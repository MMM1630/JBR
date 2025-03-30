from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NeedyProfile, HelpedNeedy
from decimal import Decimal



@receiver(post_save, sender=NeedyProfile)
def move_to_helped(sender, instance, **kwargs):
    if not instance.active:
        helped_needy = HelpedNeedy.objects.create(
            name=instance.name,
            surname=instance.surname,
            age=instance.age,
            diagnosis=instance.diagnosis,
            treatment=instance.treatment
        )

        for photo in instance.photos.all():
            helped_needy.photos.add(photo)

        helped_needy.save()



