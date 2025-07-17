from django.urls import path
from . import views

urlpatterns = [
    path("sales_chart", views.get_sales_chart, name="api/sales_chart"),
]
