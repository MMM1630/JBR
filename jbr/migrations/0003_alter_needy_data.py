# Generated by Django 5.1.6 on 2025-02-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbr', '0002_remove_needy_urgency_needy_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='needy',
            name='data',
            field=models.CharField(max_length=20, verbose_name='До какого числа сбор '),
        ),
    ]
