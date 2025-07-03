from django.db import models

from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
