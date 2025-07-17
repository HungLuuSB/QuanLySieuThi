from django.db import models

from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    price = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    stock = models.PositiveIntegerField(default=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
