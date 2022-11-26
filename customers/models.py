import datetime

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()


class Cart(models.Model):
    product = models.ForeignKey(
        Product, blank=True, null=True, on_delete=models.CASCADE, default=None
    )
    quantity = models.IntegerField(default=0)


class Customer(models.Model):
    name = models.CharField("Customer", max_length=30)
    registration_date = models.DateTimeField(default=datetime.datetime.now())
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, auto_created=True, default=None)

    def __str__(self):
        return self.name
