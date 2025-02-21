from rest_framework import serializers
from models import Patients

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Patients
        fields = ("name", 'surname', 'img', 'age', 'disease', 'urgency', 'sum', 'collected', 'active', 'description')

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('img', 'title', 'description')

class GuaranteeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('duty', 'duty_file')

class FoundersSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'surname', 'img', 'title')

class BankDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('MbankImg', 'Mbank', 'ObankImg', 'Obank', 'CompanionImg', 'Companion', 'BakaiBankImg', 'BakaiBank')