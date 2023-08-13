from django.urls import path
from .views import PlaceTypeList, PlaceList , PlaceDetail


urlpatterns = [
    path('types/', PlaceTypeList.as_view(), name='place-type-list'),
    path('places/', PlaceList.as_view(), name='place-list'),
    path('establishments/<int:pk>/', PlaceDetail.as_view(), name='place-detail'),
]
