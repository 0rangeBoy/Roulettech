from django.shortcuts import render
from rest_framework import serializers
from .models import PersonalAppText
from .models import PersonalAppImg

class PersonalAppSerializerText(serializers.ModelSerializer):
    class Meta:
        model = PersonalAppText
        fields = ('id', 'title', 'text')

class PersonalAppSerializerIMG(serializers.ModelSerializer):
    class Meta:
        model = PersonalAppImg
        fields = ('id','title', 'imgURL')