# Generated by Django 5.1.6 on 2025-03-12 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jbr', '0021_needyprofile_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='needyprofile',
            name='active',
        ),
    ]
