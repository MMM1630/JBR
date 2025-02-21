from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from jbr.choices import CHOICES_PATIENTS

class Patients(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=40)
    img = models.ImageField('Фото')
    age = models.IntegerField('Возраст')
    disease = models.CharField('Заболевание', max_length=100)
    urgency = models.CharField('Насколько срочно',max_length=255 ,choices=CHOICES_PATIENTS, null=True, blank=True)
    sum = models.CharField('Сумма сбора', max_length=100)
    collected = models.CharField('Собранная сумма', max_length=100)
    active = models.BooleanField('Активно для сбора', default=False)
    description = RichTextUploadingField('Подробнее', config_name='default')

    class Meta:
        verbose_name = 'Больные'
        verbose_name_plural = 'Больные'

class AboutUs(models.Model):
    img = models.ImageField('Логотип')
    title = models.CharField('Описание', max_length=250)
    description = RichTextUploadingField('Подробнее', config_name='default')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Guarantee(models.Model):
    duty = models.TextField('Обязанности')
    duty_file = models.FileField('Файл с информацией')

    class Meta:
        verbose_name = 'Гарантия'
        verbose_name_plural = 'Гарантия'

class Founders(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=40)
    img = models.ImageField('Фото')
    title = models.CharField('Описание', max_length=250)

    class Meta:
        verbose_name = 'Основатели'
        verbose_name_plural = 'Основатели'

class BankDetails(models.Model):
    MbankImg = models.ImageField('Мбанк лого', null=True, blank=True)
    Mbank = models.CharField('Мбанк', max_length=20)
    ObankImg = models.ImageField('ОБанк лого', null=True, blank=True)
    Obank = models.CharField('ОБанк', max_length=20)
    CompanionImg = models.ImageField('Компанион лого', null=True, blank=True)
    Companion = models.CharField('Компанион', max_length=20)
    BakaiBankImg = models.ImageField('Бакай Банк лого', null=True, blank=True)
    BakaiBank =models.CharField('Бакай Банк', max_length=20)

    class Meta:
        verbose_name = 'Банковские реквезиты'
        verbose_name_plural = 'Банковские реквезиты'
