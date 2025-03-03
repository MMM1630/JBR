# Generated by Django 5.1.6 on 2025-02-18 09:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('founder', models.CharField(max_length=50, verbose_name='Основатель')),
                ('about_us', models.TextField(verbose_name='О нас')),
            ],
        ),
        migrations.CreateModel(
            name='Guarantee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty', models.TextField(verbose_name='Обязанности')),
                ('duty_file', models.FileField(upload_to='', verbose_name='Файл с информацией')),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('disease', models.CharField(max_length=100, verbose_name='Заболевание')),
                ('sum', models.IntegerField(verbose_name='Сумма сбора')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Подробнее')),
            ],
        ),
    ]
