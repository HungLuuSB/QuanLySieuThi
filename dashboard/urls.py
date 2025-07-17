from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="dashboard/index"),
               path('add_category', views.add_category, name="dashboard/add-category")]




