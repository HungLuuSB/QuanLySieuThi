from django.shortcuts import redirect, render
from dashboard.forms import AddProductForm
from common.models import Product, Category
# Create your views here.
#


def index(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            p = Product(
                name=form.cleaned_data["product_name"],
                description=form.cleaned_data["product_desc"],
                category=Category.objects.get(id=form.cleaned_data["category"]),
            )
            p.save()
    context = {"form": AddProductForm()}
    return render(request, "dashboard/index.html")


def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            p = Product(
                name=form.cleaned_data["product_name"],
                description=form.cleaned_data["product_desc"],
                price=form.cleaned_data["product_price"],
                stock=form.cleaned_data["stock"],
                category=Category.objects.get(id=form.cleaned_data["category"]),
            )
            p.save()
    context = {"form": AddProductForm(), "categories": Category.objects.all()}
    return render(request, "dashboard/add_product.html", context)


def products(request):
    context = {"products": Product.objects.all()}
    return render(request, "dashboard/products.html", context)
