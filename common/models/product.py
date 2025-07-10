from django.db import models

from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
def __str__(self):
        return self.name