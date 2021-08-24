from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

router = DefaultRouter()
urlpatterns = [
    path('',include(router.urls)),
    path('login/',TokenPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('register/',RegisterView.as_view()),
    path('api-auth/',include('rest_framework.urls')),
    
]


