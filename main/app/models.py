from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50)
    mark = models.CharField(max_length=50)
    price = models.FloatField()
    year = models.IntegerField()

class Restoration(models.Model):
    name = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete = models.PROTECT)
    date_start = models.DateField()
    date_end = models.DateField()
    total_price = models.FloatField()

class Range(models.Model):
    result = models.IntegerField()








