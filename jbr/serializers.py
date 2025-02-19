from rest_framework import serializers
from models import Patients

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Patients
        fields = "__all__"

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"

class GuaranteeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"

class FoundersSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"

class BankDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"