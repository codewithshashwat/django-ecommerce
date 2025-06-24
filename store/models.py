from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Customer(models.Model):
    pass

class Product(models.Model):
    pass

class Order(models.Model):
    pass