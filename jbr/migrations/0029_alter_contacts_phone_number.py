# Generated by Django 5.1.6 on 2025-03-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbr', '0028_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone_number',
            field=models.CharField(default='+996', max_length=13, verbose_name='Наши контакты'),
        ),
    ]
