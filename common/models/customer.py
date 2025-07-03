from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=11)
