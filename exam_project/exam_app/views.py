from django.shortcuts import render
from rest_framework import generics
from .models import PlaceType, Place, PlaceDetail
from .serializers import PlaceTypeSerializer, PlaceSerializer


class PlaceTypeList(generics.ListAPIView):
    queryset = PlaceType.objects.all()
    serializer_class = PlaceSerializer


class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class PlaceByCityList(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = Place.objects.filter(city=city)
        else:
            queryset = Place.objects.all()
        return queryset


class PlaceByAddressList(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        address = self.request.query_params.get('address', None)
        if address is not None:
            queryset = Place.objects.filter(address__icontains=address)
        else:
            queryset = Place.objects.all()
        return queryset
    
class PlaceByNameList(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = Place.objects.filter(name__icontains=name)
        else:
            queryset = Place.objects.all()
        return queryset