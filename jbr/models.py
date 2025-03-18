from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser


class Needy(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=40)
    img = models.ImageField('Фото')
    age = models.IntegerField('Возраст')
    disease = models.CharField('Заболевание', max_length=100)
    treatment = models.CharField("Требуется лечение", max_length=255)
    sum = models.CharField('Сумма сбора', max_length=100)
    collected = models.CharField('Собранная сумма', max_length=100)
    data = models.CharField('До какого числа сбор ', max_length=20)
    active = models.BooleanField('Сбор', default=True)
    description = RichTextUploadingField('Подробнее', config_name='default')

    class Meta:
        verbose_name = 'Нуждающийся'
        verbose_name_plural = 'Нуждающийся'

    def __str__(self):
        return f"{self.name} {self.surname} - {'Сбор открыт' if self.active else 'Сбор закрыт'}"

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

# class BankDetails(models.Model):
#     needy = models.ForeignKey(Needy, on_delete=models.CASCADE, verbose_name="Банковские реквезиты для")
#     MbankImg = models.ImageField('Мбанк лого', null=True, blank=True)
#     Mbank = models.CharField('Мбанк', max_length=20)
#     ObankImg = models.ImageField('ОБанк лого', null=True, blank=True)
#     Obank = models.CharField('ОБанк', max_length=20)
#     CompanionImg = models.ImageField('Компанион лого', null=True, blank=True)
#     Companion = models.CharField('Компанион', max_length=20)
#     BakaiBankImg = models.ImageField('Бакай Банк лого', null=True, blank=True)
#     BakaiBank =models.CharField('Бакай Банк', max_length=20)
#
#     class Meta:
#         verbose_name = 'Банковские реквезиты'
#         verbose_name_plural = 'Банковские реквезиты'


class Volunteer(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=40)
    img = models.ImageField('Фото', upload_to='volunteers_photos/')

    class Meta:
        verbose_name = 'Валантеры'
        verbose_name_plural = 'Валантеры'

    def __str__(self):
        return f"{self.name} {self.surname}"


class Dokument(models.Model):
    certificate = models.ImageField("Сертификаты")

    class Meta:
        verbose_name = 'Сертификаты'
        verbose_name_plural = 'Сертификаты'


class News(models.Model):
    title = models.CharField("Описание", max_length=255)
    image = models.ImageField("Фото")
    description = RichTextUploadingField('Подробнее', config_name='default')
    create_date = models.DateField('Время добовление')
    active = models.BooleanField('Активные новости')

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural ='Новости'

    def __str__(self):
        return f"{self.title}"


class NeedyProfile(models.Model):
    patients = models.OneToOneField(Needy, on_delete=models.CASCADE, verbose_name="Личный кабинет")
    diagnosis = models.CharField("Диагноз", max_length=255)
    treatment = models.CharField("Требуется лечение", max_length=255)
    photo = models.ImageField(upload_to="needy_profiles/", blank=True, null=True, verbose_name="Фото")
    sum = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Сумма для сбора")
    collected = models.DecimalField(max_digits=50, decimal_places=2, verbose_name="Собранная сумма")
    volunteers = models.ManyToManyField("Volunteer", blank=True, verbose_name="Волонтёры")
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patients} - {self.sum} {self.collected}"

    class Meta:
        verbose_name = 'Личный кабинет'
        verbose_name_plural = 'Личный кабинет'


class Contacts(models.Model):
    title = models.CharField("Описание", max_length=255)
    phone_number = models.CharField("Наши контакты", default="+996", max_length=13)
    email = models.EmailField("@Email", default="user@gmial.com")
    geolocation = models.URLField("Наш адрес")

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.phone_number} {self.email}"
