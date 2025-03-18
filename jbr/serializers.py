from rest_framework import serializers
from jbr.models import AboutUs, Guarantee, Founders, Volunteer, Dokument, Needy, News, NeedyProfile, Contacts
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _


class NeedySerializer(serializers.ModelSerializer):
    class Meta:
        model = Needy
        fields = ("name", 'surname', 'img', 'age', 'disease', 'data', 'sum', 'collected', 'active', 'description')

class NeedyProfileSerializers(serializers.ModelSerializer):
    volunteers = serializers.SerializerMethodField()
    patients = serializers.SerializerMethodField()

    def get_volunteers(self, obj):
        return [f"{volunteer.name} {volunteer.surname}" for volunteer in obj.volunteers.all()]

    def get_patients(self, obj):
        return f"{obj.patients.name} {obj.patients.surname}"

    class Meta:
        model = NeedyProfile
        fields = ["id", "photo", "sum", "currency", "patients", "volunteers"]

    class Meta:
        model = NeedyProfile
        fields = "__all__"

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('img', 'title', 'description')

class GuaranteeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guarantee
        fields = ('duty', 'duty_file')

class FoundersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Founders
        fields = ('name', 'surname', 'img', 'title')

# class BankDetailsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = BankDetails
#         fields = ('MbankImg', 'Mbank', 'ObankImg', 'Obank', 'CompanionImg', 'Companion', 'BakaiBankImg', 'BakaiBank', 'needy')

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = "__all__"

class DokumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Dokument
        fields = "__all__"


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"

