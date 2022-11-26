from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

class Cart(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Customer(models.Model):
    name = models.CharField("Customer", max_length=30)
    registration_date = models.DateTimeField(auto_now_add=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, auto_created=True)

    def __str__(self):
        return self.name

