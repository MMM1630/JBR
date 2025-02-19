from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from jbr.models import Patients, AboutUs, Guarantee, Founders, BankDetails
from django import forms



class PatientsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Patients
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PatientsAdminForm

@admin.register(Patients)
class PatientsAdmin(admin.ModelAdmin):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    list_display = ("name", "surname", "age", "disease", "sum", "collected", "active", "description")

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

@admin.register(BankDetails)
class BankDetails(admin.ModelAdmin):
    list_display = ("Mbank", "Obank", "Companion", "BakaiBank")