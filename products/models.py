from django.db import models


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=150)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name
