from django.shortcuts import render
from common.models import Order, OrderDetails, Product, Category, category
# Create your views here.

from django.views.generic import TemplateView


def get_sales_chart(request):
    labels = []
    data = []

    queryset = Product.objects.order_by("category")
    for category in queryset:
        count = Product.objects.filter(category_id=category.id).count()
        labels.append(category.name)
        data.append(count)

    return render(
        request,
        "chartjs/index.html",
        {
            "labels": labels,
            "data": data,
        },
    )
