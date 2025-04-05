from rest_framework import serializers
from jbr.models import AboutUs, Guarantee, Founders, Volunteer, Dokument, News, NeedyProfile, Contacts, HelpedNeedy, Bank,  Application_needy, NeedyProfile, NeedyProfilePhoto, DokumentsNeedy, VolunteerAssignment, NeedyDisplay, NeedyDisplayDocument, NeedyDisplayPhoto, HelpedNeedyPhoto 
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
        fields = ['id',  'name', 'surname', 'img']
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

    def get_photos(self, obj):
        request = self.context.get('request')
        photos = HelpedNeedyPhoto.objects.filter(helped_needy=obj)
        return [{"photo_url": request.build_absolute_uri(photo.photo.url)} for photo in photos if photo.photo]
    



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
    
    def update(self, instance, validated_data):
        instance.collected = validated_data.get('collected', instance.collected)
        instance.save()
        return instance


class NeedyProfilePhotoSerializers(serializers.ModelSerializer):
    img = serializers.ImageField(source="photo.url")
    class Meta:
        model = NeedyProfilePhoto
        fields = "__all__"


class DokumentsNeedySerializers(serializers.ModelSerializer):
    file_url = serializers.FileField(source="document.url")
    class Meta:
        model = DokumentsNeedy
        fields = "__all__"  


class VolunteerAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerAssignment
        fields = '__all__'


class AddAmountSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)

    def update(self, instance, validated_data):
        instance.add_to_collected(validated_data['amount'])
        return instance


class NeedyDisplayPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeedyDisplayPhoto
        fields = ["photo"]

class NeedyDisplayDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeedyDisplayDocument
        fields = ["document"]

class NeedyDisplaySerializers(serializers.ModelSerializer):
    photos = NeedyDisplayPhotoSerializer(many=True, read_only=True)
    documents = NeedyDisplayDocumentSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.collected = validated_data.get('collected', instance.collected)
        instance.save()
        return instance

    class Meta:
        model = NeedyDisplay
        fields = "__all__"



class UpdateCollectedSerializer(serializers.Serializer):
    collected = serializers.DecimalField(max_digits=10, decimal_places=2)

    def update(self, instance, validated_data):
        collected_value = validated_data.get('collected', instance.collected)
        
        instance.collected = collected_value
        instance.save()

        try:
            needy_display = NeedyDisplay.objects.get(needy_profile=instance)
            needy_display.collected = collected_value
            needy_display.save()
        except NeedyDisplay.DoesNotExist:
            pass 

        return instance