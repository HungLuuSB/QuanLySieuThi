from django.db import models
from .customer import Customer


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.CASCADE
    )
    customer_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=11)
    shipping_address = models.TextField()
    grand_total = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(max_length=15, default="PENDING")
