from django.db import models
from products.models import Products

class Vendors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    city = models.CharField(max_length=150)
    products = models.ManyToManyField(Products)


    def __str__(self):
        return self.name
