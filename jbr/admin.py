from pyclbr import Class
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from jbr.models import AboutUs, Guarantee, Founders, Volunteer, Dokument, News, NeedyProfile, Contacts, HelpedNeedy, Bank, NeedyProfilePhoto, DokumentsNeedy, Application_needy, NeedyDisplay, NeedyDisplayPhoto, NeedyDisplayDocument, HelpedNeedyPhoto
from django import forms
from django.utils.html import format_html


class NeedyProfilePhotoInline(admin.TabularInline):
    model = NeedyProfilePhoto  
    extra = 1  

class DokumentsNeedyInline(admin.TabularInline):
    model = DokumentsNeedy
    extra = 1
    
class VolunteerNeedyInline(admin.TabularInline):
    model = Volunteer
    extra = 1


@admin.register(NeedyProfile)
class NeedyProfileAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "diagnosis", "treatment", "sum", "collected", "active")  
    list_filter = ("phone_number", "active")  
    list_editable = ("active",)
    search_fields = ("phone_number",)  
    inlines = [NeedyProfilePhotoInline, DokumentsNeedyInline, VolunteerNeedyInline]  



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


class HelpedNeedyPhotoInline(admin.TabularInline):
    model = HelpedNeedyPhoto
    extra = 1

@admin.register(HelpedNeedy)
class HelpedNeedyAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'diagnosis', 'treatment')
    list_filter = ('name', 'surname', 'age')
    inlines = [HelpedNeedyPhotoInline]


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('urls', 'display_qr')


    def display_qr(self, obj):
        if obj.qr_code:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 10px;" />', obj.qr_code.url)
        return "Нет QR кода"
    display_qr.short_description = "QR код"
    

@admin.register(Application_needy)
class AplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')


class NeedyDisplayPhotoInline(admin.TabularInline):
    model = NeedyDisplayPhoto
    extra = 1

class NeedyDisplayDocumentInline(admin.TabularInline):
    model = NeedyDisplayDocument
    extra = 1

@admin.register(NeedyDisplay)
class NeedyDislplayAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age')
    inlines = [NeedyDisplayPhotoInline, NeedyDisplayDocumentInline]

@admin.register(NeedyDisplayPhoto)
class NeedyDisplayPhotoAdmin(admin.ModelAdmin):
    list_display = ("needy_display", "photo")

@admin.register(NeedyDisplayDocument)
class NeedyDisplayDocumentAdmin(admin.ModelAdmin):
    list_display = ("needy_display", "document")