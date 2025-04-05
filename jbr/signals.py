from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NeedyProfile, HelpedNeedy, NeedyDisplay, NeedyDisplayPhoto, NeedyDisplayDocument, DokumentsNeedy, NeedyProfilePhoto, HelpedNeedyPhoto
from decimal import Decimal
import logging


logger = logging.getLogger(__name__)

@receiver(post_save, sender=NeedyProfile)
def move_to_helped(sender, instance, **kwargs):
    if instance.collected is not None and instance.sum is not None:
        if instance.collected >= instance.sum:
            logger.info(f"Moving NeedyProfile {instance.id} to HelpedNeedy...")
            
            def move():
                helped_needy = HelpedNeedy.objects.create(
                    name=instance.name,
                    surname=instance.surname,
                    age=instance.age,
                    diagnosis=instance.diagnosis,
                    treatment=instance.treatment,
                    sum=instance.sum,
                    collected=instance.collected,
                )

                photos = NeedyProfilePhoto.objects.filter(needy_profile=instance)
                for photo in photos:
                    HelpedNeedyPhoto.objects.create(helped_needy=helped_needy, photo=photo.photo)

                logger.info(f"Created HelpedNeedy for {instance.id}. Deleting NeedyProfile...")
                instance.delete()
            
            transaction.on_commit(move)
        else:
            logger.warning(f"Conditions not met for moving NeedyProfile {instance.id}: collected={instance.collected}, sum={instance.sum}")
    else:
        logger.warning(f"NeedyProfile {instance.id} has missing 'collected' or 'sum' value.")


logger = logging.getLogger(__name__)

@receiver(post_save, sender=NeedyProfile)
def move_to_display(sender, instance, created, **kwargs):
    if created: 
        def process_after_commit():
            needy_display = NeedyDisplay.objects.create(
                name=instance.name,
                surname=instance.surname,
                age=instance.age,
                diagnosis=instance.diagnosis,
                treatment=instance.treatment,
                sum=instance.sum,
                collected=instance.collected,
            )

            photos = NeedyProfilePhoto.objects.filter(needy_profile=instance)
            for photo in photos:
                NeedyDisplayPhoto.objects.create(needy_display=needy_display, photo=photo.photo)

            documents = DokumentsNeedy.objects.filter(needy_profile=instance)
            for document in documents:
                NeedyDisplayDocument.objects.create(needy_display=needy_display, document=document.dokument)

        transaction.on_commit(process_after_commit)
    else:
        try:
            needy_display = NeedyDisplay.objects.get(needy_profile=instance)
            if needy_display.collected != instance.collected:
                needy_display.collected = instance.collected
                needy_display.save()
                logger.info(f"Обновлено поле collected для {instance.name} {instance.surname}")
        except NeedyDisplay.DoesNotExist:
            logger.warning(f"Не найден дисплей для {instance.name} {instance.surname}")