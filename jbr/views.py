from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from jbr.models import Needy, AboutUs, Guarantee, Founders, Volunteer, Dokument, News, NeedyProfile, Contacts
from jbr.serializers import NeedySerializer, AboutUsSerializer, GuaranteeSerializers, FoundersSerializers, \
    VolunteerSerializer, DokumentSerializers, NewsSerializers, NeedyProfileSerializers,ContactsSerializers


class NeedyView(generics.ListCreateAPIView):
    queryset = Needy.objects.all()
    serializer_class = NeedySerializer

class NeedyProfileView(generics.ListCreateAPIView):
    queryset = NeedyProfile.objects.all()
    serializer_class = NeedyProfileSerializers

class AboutUsView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class GuaranteeView(generics.ListAPIView):
    queryset = Guarantee.objects.all()
    serializer_class = GuaranteeSerializers

class FoundersView(generics.ListAPIView):
    queryset = Founders.objects.all()
    serializer_class = FoundersSerializers

# class BankDetailsView(generics.ListAPIView):
#     queryset = BankDetails.objects.all()
#     serializer_class = BankDetailsSerializers

class VolunteerView(APIView):
    def get(self, request, volunteer_id=None):
        if volunteer_id:
            volunteer = get_object_or_404(Volunteer, id=volunteer_id)
            serializer = VolunteerSerializer(volunteer, context={'request': request})
        else:
            volunteers = Volunteer.objects.all()
            serializer = VolunteerSerializer(volunteers, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VolunteerSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'Success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': False, 'message': 'Error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DokumentView(generics.ListAPIView):
    queryset = Dokument.objects.all()
    serializer_class = DokumentSerializers


class NewsView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class ContactsView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers


