
from django.contrib import admin
from django.urls import path
from exam_app.views import PlaceTypeList, PlaceList , PlaceDetail, PlaceByCityList,PlaceByAddressList, PlaceByNameList
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="city_directory_API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('types/', PlaceTypeList.as_view(), name='place-type-list'),
    path('places/', PlaceList.as_view(), name='place-list'),
    path('places/<int:pk>/', PlaceDetail.as_view(), name='place-detail'),
    path('places/by-city/', PlaceByCityList.as_view(), name='place-by-city-list'),
    path('places/by-address/', PlaceByAddressList.as_view(), name='place-by-address-list'),
    path('places/by-name/', PlaceByNameList.as_view(), name='place-by-name-list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
