from django.db import models
from django.utils import timezone


class Cart(models.Model):
    name = models.CharField(max_length=50, default='cart')


class Customer(models.Model):
    name = models.CharField(max_length=30)
    registration_date = models.DateTimeField(default=timezone.now)
    # cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    #
    # @property
    # def cart_name(self):
    #     return self.cart.name
    #
    # @cart_name.setter
    # def cart_name(self, value):
    #     self.cart, _ = Cart.objects.get_or_create(name=value)
