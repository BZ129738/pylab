from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(max_length=350)
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    stock = models.IntegerField(default=0)


class Buty(models.Model):
    brand = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=350)
    size = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    class Meta:
        verbose_name_plural = "buty"
