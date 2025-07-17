from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dashboard/index"),
    path("add_order/", views.add_order, name="dashboard/add_order")
]
