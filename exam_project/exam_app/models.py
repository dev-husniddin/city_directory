from django.db import models

class PlaceType(models.Model):
    name = models.CharField(max_length=100)

class Place(models.Model):

    name = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    category = models.ForeignKey(PlaceType, on_delete=models.CASCADE)

    address = models.CharField('Адрес', max_length=200)
    city = models.CharField("Город", max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    alt_phone = models.CharField('Доп.телефон', max_length=20, blank=True)
    email = models.EmailField('Email')
    working_hours = models.CharField('Время работы', max_length=20)
    photos = models.ImageField(upload_to='establishment_photos/', blank=True)

 
 
class City(models.Model):
    
    name = models.CharField('Название', max_length=150)

    
class Category(models.Model):
    category = models.ForeignKey(PlaceType, on_delete=models.CASCADE, related_name='places')

class PlaceDetail(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)