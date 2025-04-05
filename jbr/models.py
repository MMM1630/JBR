from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import random
import string
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
from django.db.models import F



User = get_user_model()


class CustomUser(AbstractUser):
    username = None 
    phone_number = models.CharField("Номер телефона", max_length=15, unique=True)

    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions")

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []



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


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

class NeedyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=15, unique=True, null=True, blank=True)
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20)
    age = models.IntegerField("Возраст", null=True, blank=True)
    diagnosis = models.CharField("Диагноз", max_length=255, null=True, blank=True)
    treatment = models.CharField("Требуется лечение", max_length=255, null=True, blank=True)
    sum = models.IntegerField(verbose_name="Сумма для сбора", null=True, blank=True)
    sum_usd = models.FloatField("Сумма в долларах", null=True, blank=True, editable=False)
    collected = models.IntegerField(verbose_name="Собранная сумма", null=True, blank=True)
    active = models.BooleanField("Сбор", default=True, null=True, blank=True)
    password = models.CharField("Пароль", max_length=8, default=generate_password, editable=False)

    def save(self, *args, **kwargs):
        if not self.user and self.phone_number:  
            username = f"user_{self.phone_number}"  
            password = generate_password()
            user = User.objects.create_user(username=username, password=password)
            self.user = user  
            self.password = password  

        if self.sum:
            exchange_rate = 0.012 
            self.sum_usd = round(self.sum * exchange_rate, 2)
        else:
            self.sum_usd = None

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Личный кабинет для нуждающегося"
        verbose_name_plural = "Личный кабинет для нуждающегося"


class NeedyProfilePhoto(models.Model):
    needy_profile = models.ForeignKey(NeedyProfile, on_delete=models.CASCADE, verbose_name="Профиль")
    photo = models.ImageField(upload_to="needy_profiles/photos/", verbose_name="Фото")
    
    class Meta:
        verbose_name = "Фото профиля"
        verbose_name_plural = "Фотографии профиля"

    
class DokumentsNeedy(models.Model):
    needy_profile = models.ForeignKey(NeedyProfile, on_delete=models.CASCADE, verbose_name="Документы нуждающегося")
    dokument = models.FileField(upload_to="needy_profiles/dokuments/", verbose_name="Документ")


    def __str__(self):
        return f"Документы для {self.needy_profile.phone_number}"

    class Meta:
        verbose_name = "Документы нуждающегося"
        verbose_name_plural = "Документы нуждающегося"


class Volunteer(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=40)
    img = models.ImageField('Фото', upload_to='volunteers_photos/')
    needy_profile = models.ForeignKey(NeedyProfile, on_delete=models.CASCADE, related_name="volunteers", null=True, blank=True)


    class Meta:
        verbose_name = 'Валантеры'
        verbose_name_plural = 'Валантеры'

    def __str__(self):
        return f"{self.name} {self.surname}"


class VolunteerAssignment(models.Model):
    needy_profile = models.ForeignKey(NeedyProfile, on_delete=models.CASCADE)
    volunteer_profile = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='assigned')  

    def __str__(self):
        return f"Volunteer {self.volunteer_profile.name} assigned to {self.needy_profile.name}"


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


class HelpedNeedy(models.Model):
    img = models.ImageField(upload_to="helped_needy/",  verbose_name="Фото")
    name = models.CharField("Имя", max_length=255)
    surname = models.CharField("Фамилия", max_length=255)
    age = models.IntegerField('Возраст')
    diagnosis = models.CharField("Диагноз", max_length=255)
    treatment = models.CharField("Лечение", max_length=255)
    sum = models.IntegerField(verbose_name="Сумма для сбора", null=True, blank=True)
    collected = models.IntegerField(verbose_name="Собранная сумма", null=True, blank=True)
    photos = models.ManyToManyField(NeedyProfilePhoto, related_name='helped_needy_photos', blank=True)


    class Meta:
        verbose_name = "Кому помогли"
        verbose_name_plural = "Кому помогли"

    def __str__(self):
        return f"{self.name} {self.surname}"


class HelpedNeedyPhoto(models.Model):
    helped_needy = models.ForeignKey(HelpedNeedy, on_delete=models.CASCADE,verbose_name="Фото нужадющегося")
    photo = models.ImageField(upload_to="helped_needy_profiles/photos/", verbose_name="Фото")

    class Meta:
        verbose_name = "Фото нуждающегося"
        verbose_name_plural = "Фото нуждающегося"


class Bank(models.Model):
    urls = models.URLField("Ссылка на банк")
    qr_code = models.ImageField("QR код нужадющегося")

    class Meta:
        verbose_name = "Реквизиты нуждающегося"
        verbose_name_plural = "Реквизиты нуждающегося"

    def __str__(self):
        return f"{self.qr_code}"


class Application_needy(models.Model):
    name = models.CharField("Имя", max_length=255)
    phone_number = models.CharField("Номер телефона", max_length=255)


    class Meta:
        verbose_name = "Заявка нуждающегося"
        verbose_name_plural = "Заявка нуждающегося"


class NeedyDisplay(models.Model):
    needy_profile = models.ForeignKey(NeedyProfile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20)
    age = models.IntegerField("Возраст")
    diagnosis = models.CharField("Диагноз", max_length=255, null=True, blank=True)
    treatment = models.CharField("Требуется лечение", max_length=255, null=True, blank=True)
    sum = models.IntegerField(verbose_name="Сумма для сбора", null=True, blank=True)
    sum_usd = models.FloatField("Сумма в долларах", null=True, blank=True)  
    collected = models.IntegerField(verbose_name="Собранная сумма", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.sum:
            exchange_rate = 0.012 
            self.sum_usd = round(self.sum * exchange_rate, 2)
        else:
            self.sum_usd = None
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = "Дисплей нуждающегося"
        verbose_name_plural = "Дисплей нуждающегося"


class NeedyDisplayPhoto(models.Model):
    needy_display = models.ForeignKey(NeedyDisplay, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField("Фотография", upload_to="needy_display/photos/")

    class Meta:
        verbose_name = "Фото дисплея"
        verbose_name_plural = "Фотографии дисплея"


class NeedyDisplayDocument(models.Model):
    needy_display = models.ForeignKey(NeedyDisplay, on_delete=models.CASCADE, related_name="documents")
    document = models.FileField("Документ", upload_to="needy_display/documents/")

    class Meta:
        verbose_name = "Документ дисплея"
        verbose_name_plural = "Документы дисплея"