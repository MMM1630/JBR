# Generated by Django 5.1.6 on 2025-03-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbr', '0037_remove_needyprofile_is_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='needyprofile',
            name='is_closed',
            field=models.BooleanField(default=False),
        ),
    ]
