from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dashboard/index"),
    path("order", views.index, name="dashboard/order"),
    path("products", views.products, name="dashboard/products"),
    path("products/add_product", views.add_product, name="dashboard/add_product"),
]
