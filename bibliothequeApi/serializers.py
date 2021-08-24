from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import transaction
from django.contrib.auth.models import Group
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *

class TokenPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super(TokenPairSerializer,self).validate(attrs)
        data['is_admin'] = self.user.is_superuser
        data['groups'] = [x.name for x in self.user.groups.all()]
        data['username']= self.user.username
        data['first_name']= self.user.first_name
        data['last_name']= self.user.last_name

        return data

        #for x in self.user.groups:
            #return x.name
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = "is_active" ,"is_staff",
        exlcude = "last_login","is_staff", "date_joined","user_permission",

        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
            
        }
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    email = serializers.CharField(required = True)
    adresse = serializers.CharField(required = True)
    telephone = serializers.CharField(required = True)

class BibliothecaireSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    def create(self, obj):
        user_obj = obj.pop('user')
        user = User(
            username = user_obj['username'],
            first_name = user_obj['first_name'],
            last_name = user_obj['last_name'],

        )
        password = user_obj['password']
        user.is_active = True
        user.set_password(password)
        bibliothecaire = Bibliothecaire(
            user = user,
            date_naissance = obj['date_naissance'],
            matricule = obj['matricule']
        )
        user.save()
        bibliothecaire.save()
        return bibliothecaire
    class Meta:
        model = Bibliothecaire
        fields = '__all__'
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = '__all__'
class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    def create(self, obj):
        user_obj = obj.pop('user')
        user = User(
            username = user_obj['username'],
            first_name = user_obj['first_name'],
            last_name = user_obj['last_name'],

        )
        password = user_obj['password']
        user.is_active = True
        user.set_password(password)
        client = Client(
            user = user,
            adresse = obj['adresse'],
            telephone = obj['telephone']
        )
        user.save()
        client.save()
        return client
    class Meta:
        model = Client
        fields = '__all__'
             
class MesLivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesLivre
        fields = '__all__'

class VenteSerializer(serializers.ModelSerializer):
  class Meta:
      model = Vente
      fields = '__all__'


