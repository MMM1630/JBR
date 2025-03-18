from pyclbr import Class
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from jbr.models import Needy, AboutUs, Guarantee, Founders, Volunteer, Dokument, News, NeedyProfile, Contacts
from django import forms
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django_select2.forms import Select2MultipleWidget



class NeedyAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Needy
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = NeedyAdminForm

@admin.register(Needy)
class NeedyAdmin(admin.ModelAdmin):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    list_display = ("name", "surname", "age", "disease", "treatment", "data", "sum", "collected", "active")
    list_editable = ("active",)
    list_filter = ("name", "surname")



class NeedyProfileForm(forms.ModelForm):
    class Meta:
        model = NeedyProfile
        fields = '__all__'
        widgets = {
            'volunteers': Select2MultipleWidget,
        }

@admin.register(NeedyProfile)
class NeedyProfileAdmin(admin.ModelAdmin):
    form = NeedyProfileForm
    list_display = ("patients", "display_photo", "diagnosis", "treatment", "sum", "collected", "display_volunteers")
    list_filter = ("patients",)
    search_fields = ("patients__name", "volunteers__name")

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />', obj.photo.url)
        return "Нет фото"
    display_photo.short_description = "Фото"

    def display_volunteers(self, obj):
        return ", ".join([v.name for v in obj.volunteers.all()]) if obj.volunteers.exists() else "Нет волонтёров"
    display_volunteers.short_description = "Волонтёры"


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    model = AboutUs
    list_display = ("img", "title", "description")

@admin.register(Guarantee)
class GuaranteeAdmin(admin.ModelAdmin):
    list_display = ("duty", "duty_file")


@admin.register(Founders)
class FoundersAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "img", "title")

# @admin.register(BankDetails)
# class BankDetails(admin.ModelAdmin):
#     list_display = ("needy","MbankImg", "Mbank", "ObankImg", "Obank", "CompanionImg", "Companion", "BakaiBankImg", "BakaiBank")

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'img')


@admin.register(Dokument)
class DokumentAdmin(admin.ModelAdmin):
    list_display = ('certificate',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'create_date', 'active')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_number', 'email', 'geolocation')


