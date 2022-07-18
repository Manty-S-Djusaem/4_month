from django.db import models


# Create your models here.


class PC(models.Model):
    name = models.CharField(max_length=255)
    memory = models.IntegerField(default=8)
    price = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)


class Categories(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

