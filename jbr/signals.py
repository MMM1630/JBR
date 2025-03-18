from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Needy, NeedyProfile
from decimal import Decimal

@receiver(post_save, sender=Needy)
def create_needy_profile(sender, instance, created, **kwargs):
    if created:
        sum_value = instance.sum
        if isinstance(sum_value, str):
            sum_value = sum_value.replace(" ", "")
            try:
                sum_value = Decimal(sum_value)
            except:
                sum_value = Decimal(0)

        NeedyProfile.objects.create(
            patients=instance,
            photo=instance.img,
            diagnosis=instance.disease,
            treatment =instance.treatment,
            sum=sum_value,
            collected=Decimal(0),
            is_closed=False,
        )


@receiver(post_save, sender=NeedyProfile)
def check_fundraising_status(sender, instance, **kwargs):
    print("Checking fundraising status...")

    collected_value = Decimal(instance.collected)
    sum_value = Decimal(instance.sum)

    if collected_value >= sum_value and not instance.is_closed:
        print("Closing fundraising...")

        with transaction.atomic():
            instance.is_closed = True
            instance.save(update_fields=["is_closed"])
            print("Fundraising closed.")

    else:
        print(f"Fundraising not closed: {collected_value} >= {sum_value}")