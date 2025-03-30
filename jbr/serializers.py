from rest_framework import serializers
from jbr.models import AboutUs, Guarantee, Founders, Volunteer, Dokument, News, NeedyProfile, Contacts, HelpedNeedy, Bank,  Application_needy, NeedyProfile, NeedyProfilePhoto, DokumentsNeedy, VolunteerAssignment
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _


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
        fields = ('id','name', 'surname', 'img', 'title')


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = ['id', 'user', 'name', 'surname', 'img']
        extra_kwargs = {
            'name': {'help_text': 'Имя волонтера'},
            'surname': {'help_text': 'Фамилия волонтера'},
            'img': {'help_text': 'Фото волонтера'}
        }

    def get_img(self, obj):
        request = self.context.get('request')  
        print(f"Debug: img path - {obj.img}")
        if obj.img:
            img_url = request.build_absolute_uri(obj.img.url)
            print(f"Debug: img absolute URL - {img_url}")
            return img_url
        return None

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

class HelpedNeedySerializers(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    class Meta:
        model = HelpedNeedy
        fields = "__all__"

    def create(self, validated_data):
        photos = validated_data.pop('photos', [])  
        helped_needy = HelpedNeedy.objects.create(**validated_data)

        if photos:
            helped_needy.photos.set(photos) 
            helped_needy.img = photos[0].image 
            helped_needy.save()

        return helped_needy
    
    def get_photos(self, obj):
        return [photo.photo.url for photo in obj.photos.all()]


class BankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"

class AplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application_needy
        fields = "__all__"


class NeedyProfileSerializers(serializers.ModelSerializer):
    documents = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField() 
    volunteers = VolunteerSerializer(many=True, read_only=True)

    class Meta:
        model = NeedyProfile
        fields = "__all__"

    def get_documents(self, obj):
        request = self.context.get('request')  
        documents = DokumentsNeedy.objects.filter(needy_profile=obj)
        return [{"file_url": request.build_absolute_uri(doc.dokument.url)} for doc in documents if doc.dokument]

    def get_photos(self, obj):
        request = self.context.get('request')
        photos = NeedyProfilePhoto.objects.filter(needy_profile=obj)
        return [{"photo_url": request.build_absolute_uri(photo.photo.url)} for photo in photos if photo.photo]
    
    def get_img(self, obj):
        request = self.context.get('request')
        img = Volunteer.objects.filter(needy_profile=obj)
        return [{"volunteer_url": request.build_absolute_uri(img.img.url) } for img in img if img.img] 


class NeedyProfilePhotoSerializers(serializers.ModelSerializer):
    img = serializers.ImageField(source="photo.url")

    class Meta:
        model = NeedyProfilePhoto
        fields = ["img"]  


class DokumentsNeedySerializers(serializers.ModelSerializer):
    file_url = serializers.FileField(source="document.url")

    class Meta:
        model = DokumentsNeedy
        fields = "__all__"  


class VolunteerAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerAssignment
        fields = '__all__'