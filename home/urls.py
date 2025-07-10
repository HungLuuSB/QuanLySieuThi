from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home'),  # ← Gắn trang chủ
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),

]
