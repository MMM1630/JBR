from rest_framework import generics
from rest_framework.generics import ListAPIView
from jbr.models import Patients, AboutUs, Guarantee, Founders, BankDetails
from jbr.serializers import PatientsSerializer, AboutUsSerializer, GuaranteeSerializers, FoundersSerializers, \
    BankDetailsSerializers


class PatientsView(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class AboutUsView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class GuaranteeView(generics,ListAPIView):
    queryset = Guarantee.objects.all()
    serializer_class = GuaranteeSerializers

class FoundersView(generics.ListAPIView):
    queryset = Founders.objects.all()
    serializer_class = FoundersSerializers

class BankDetailsView(generics.ListAPIView):
    queryset = BankDetails.objects.all()
    serializer_class = BankDetailsSerializers