from django.shortcuts import redirect, render
from dashboard.forms import AddProductForm, AddCategoryForm
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




def add_category(request):
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            c = Category(
                name = form.cleaned_data['category_name']
            )
            c.save()
    context = {"form": AddCategoryForm()}
    return render(request, "dashboard/add_category.html", context)

