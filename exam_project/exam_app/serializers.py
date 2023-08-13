from rest_framework import serializers
from .models import PlaceType, Place, PlaceDetail

class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model =PlaceType
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model =Place
        fields = '__all__'

class PlaceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =PlaceDetail
        fields = '__all__'