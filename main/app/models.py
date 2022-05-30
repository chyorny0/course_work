from django.db import models


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
    resultnumber = models.IntegerField()
    result = models.IntegerField()

class RangeVoteAdd(models.Model):
    restoration1 = models.ForeignKey(Restoration, related_name='restoration1', on_delete=models.PROTECT)
    restoration2 = models.ForeignKey(Restoration, related_name='restoration2', on_delete=models.PROTECT)
    restoration3 = models.ForeignKey(Restoration, related_name='restoration3', on_delete=models.PROTECT)
    restoration4 = models.ForeignKey(Restoration, related_name='restoration4', on_delete=models.PROTECT)
    









