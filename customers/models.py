from django.db import models


class Customer(models.Model):
    name = models.CharField('Customer', max_length=30)
    registration_date = models.DateTimeField(auto_now_add=True)
    # Cart = models.OneToOneField(Cart, on_delete=models.CASCADE)


class Cart(models.Model):
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
