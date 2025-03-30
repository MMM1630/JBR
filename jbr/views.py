from rest_framework import generics, status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from decimal import Decimal
from rest_framework.views import APIView
from jbr.models import  AboutUs, Guarantee, Founders, Volunteer, Dokument, News, Contacts, HelpedNeedy, Bank, Application_needy, NeedyProfile
from jbr.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests
import os



class NeedyProfileView(viewsets.ModelViewSet):
    queryset = NeedyProfile.objects.all()
    serializer_class = NeedyProfileSerializers
    permission_classes = [AllowAny]  

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return NeedyProfile.objects.filter(user=self.request.user)
        return NeedyProfile.objects.all()

    def perform_create(self, serializer):
        needy_profile = serializer.save()  

        if needy_profile.user:
            user = needy_profile.user
            refresh = RefreshToken.for_user(user)
            self.access_token = str(refresh.access_token)
            self.refresh_token = str(refresh)
        else:
            self.access_token = None
            self.refresh_token = None

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if hasattr(self, "access_token") and self.access_token:
            response.data["access"] = self.access_token
            response.data["refresh"] = self.refresh_token

        return response


class AboutUsView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class GuaranteeView(generics.ListAPIView):
    queryset = Guarantee.objects.all()
    serializer_class = GuaranteeSerializers

class FoundersView(generics.ListAPIView):
    queryset = Founders.objects.all()
    serializer_class = FoundersSerializers


class VolunteerView(generics.ListCreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [AllowAny]  

    def perform_create(self, serializer):
        volunteer_profile = serializer.save()  
        user = volunteer_profile.user  
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            "message": "VolunteerProfile успешно создан",
            "access": access_token,
            "refresh": str(refresh),
            "phone_number": volunteer_profile.phone_number
        }, status=status.HTTP_201_CREATED)


class VolunteerAssignment(viewsets.ModelViewSet):
    queryset = VolunteerAssignment.objects.all()
    serializer_class = VolunteerAssignmentSerializer
    permission_classes = [AllowAny]  

    def perform_create(self, serializer):
        needy_id = self.request.data.get('needy_profile')
        volunteer_id = self.request.data.get('volunteer_profile')

        assignment = VolunteerAssignment.objects.create(
            needy_profile_id=needy_id, 
            volunteer_profile_id=volunteer_id
        )
        return Response(VolunteerAssignmentSerializer(assignment).data, status=status.HTTP_201_CREATED)



class DokumentView(generics.ListAPIView):
    queryset = Dokument.objects.all()
    serializer_class = DokumentSerializers


class NewsView(APIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class ContactsView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers


class HelpedNeedyView(generics.ListAPIView):
    queryset = HelpedNeedy.objects.all()  
    serializer_class = HelpedNeedySerializers


class BankView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class =  BankSerializers




TELEGRAM_BOT_TOKEN = "7699655524:AAEzQoU_cTWp5A8hsTOvPW_3E5bOD2u2i0A"
TELEGRAM_CHAT_ID = -1002694201505

@method_decorator(csrf_exempt, name='dispatch')
class ApplicationView(generics.ListCreateAPIView):  
    serializer_class = AplicationSerializers
    queryset = Application_needy.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            application_needy = serializer.save()

            try:
                message = (
                    f"💬 *Новая заявка от нуждающегося!*\n\n"
                    f"🤕 *Имя* {application_needy.name}\n"
                    f"📞 *Телефон* {application_needy.phone_number}\n"
                )

                url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message,
                    "parse_mode": "Markdown"
                }

                response = requests.post(url, json=payload)

                if response.status_code == 200:
                    print("✅ Сообщение успешно отправлено!")
                else:
                    print(f"⚠️ Ошибка при отправке сообщения. Ответ: {response.text}")

            except Exception as e:
                print(f"❌ Ошибка отправки сообщения в Telegram: {e}")
                return Response({"Ошибка": "Не удалось отправить сообщение в Telegram"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)