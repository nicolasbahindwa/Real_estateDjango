from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='profile.gender')
    phone_number = PhoneNumberField(source='profile.phone_number')
    profile_photo = serializers.CharField(source='profile.profile_photo')
    city = serializers.CharField(source='profile.city')
    country=serializers.CharField(source='profile.country')
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.CharField(source='get_full_name')
    top_seller = serializers.BooleanField(source='profile.top_seller')


    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'gender',
            'phone_number',
            'profile_photo',
            'city',
            'country',
            'top_seller',
        ]
    
    def get_first_name(self, obj):
        return obj.first_name
    
    def get_last_name(self, obj):
        return obj.last_name
