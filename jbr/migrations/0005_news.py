# Generated by Django 5.1.6 on 2025-03-04 10:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jbr', '0004_alter_qrcode_patients'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Подробнее')),
                ('create_date', models.DateField(verbose_name='Время добовление')),
                ('active', models.BooleanField(verbose_name='Активные новости')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
