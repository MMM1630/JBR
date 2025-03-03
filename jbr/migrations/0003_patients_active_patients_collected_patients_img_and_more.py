# Generated by Django 5.1.6 on 2025-02-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbr', '0002_alter_aboutus_options_alter_guarantee_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Активно для сбора'),
        ),
        migrations.AddField(
            model_name='patients',
            name='collected',
            field=models.CharField(default=1, max_length=100, verbose_name='Собранная сумма'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patients',
            name='img',
            field=models.ImageField(default=1, upload_to='', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patients',
            name='sum',
            field=models.CharField(max_length=100, verbose_name='Сумма сбора'),
        ),
    ]
