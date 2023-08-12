from django.shortcuts import render
from rest_framework import generics
from .models import PlaceType, Place
from .serializers import PlaceTypeSerializer, PlaceSerializer


class PlaceTypeList(generics.ListAPIView):
    queryset = PlaceType.objects.all()
    serializer_class = PlaceSerializer


class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class EstablishmentDetail(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


