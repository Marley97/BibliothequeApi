from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, BasePermission
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
 
class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer

class RegisterView(APIView):
    serializer_class = RegisterSerializer
    permission_classes = AllowAny,
    def post(self, request, format=None):
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        email = request.data.get('email')
        adresse = request.data.get('adresse')
        telephone = request.data.get('telephone')

        user_obj = User(
        username = username,
        first_name = first_name,
        last_name = last_name
        )
        user_obj.set_password(password)
        user_obj.email = email
        user_obj.save()
        utilisateur_obj = Client(
        user = user_obj,
        adresse = adresse,
        telephone = telephone
        )
        utilisateur_obj.save()
        return Response({'status':'Success'},201)







#class CategorieViewset(viewsets.ModelViewSet):
    #serializer_class = CategorieSerializer
    #queryset = Categorie.objects.all()
