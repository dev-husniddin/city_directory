from rest_framework import serializers
from .models import PlaceType, Place

class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model =PlaceType
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model =Place
        fields = '__all__'
