from rest_framework import serializers
from . import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Our_teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Our_team
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.About
        fields = '__all__'
        

class Contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact_info
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ('full_name', 'email', 'subjects', 'message')

class NewletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Newletter
        fields = '__all__'

        
class ReseauxSociauSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReseauxSociau
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only':True}}
    def create(self, validated_data):
        user=User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
           
        
        