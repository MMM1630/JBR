# Generated by Django 5.1.6 on 2025-03-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbr', '0017_alter_needyprofile_volunteer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='needyprofile',
            name='volunteer',
        ),
        migrations.AddField(
            model_name='needyprofile',
            name='volunteers',
            field=models.ManyToManyField(blank=True, to='jbr.volunteer', verbose_name='Волонтёры'),
        ),
    ]
