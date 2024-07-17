from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonalAppSerializerText
from .serializers import PersonalAppSerializerIMG
from .models import PersonalAppImg
from .models import PersonalAppText

# Create your views here.

class PersonalAppViewText(viewsets.ModelViewSet):
    serializer_class = PersonalAppSerializerText
    queryset = PersonalAppText.objects.all()

class PersonalAppViewIMG(viewsets.ModelViewSet):
    serializer_class = PersonalAppSerializerIMG
    queryset = PersonalAppImg.objects.all()