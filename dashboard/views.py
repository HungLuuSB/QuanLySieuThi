from django.shortcuts import redirect, render
from dashboard.forms import AddProductForm, AddOrderForm
from common.models import Product, Category, Order
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

def add_order(request):
    if request.method == "POST":
        form = AddOrderForm(request.POST)
        if form.is_valid():
            o = Order (
                customer = None,
                customer_name=form.cleaned_data["customer_name"],
                customer_phone=form.cleaned_data["customer_phone"],
                shipping_address=form.cleaned_data["shipping_address"],
                grand_total=form.cleaned_data["grand_total"],
                status=form.cleaned_data["status"]
            )
            print(o)
            o.save()
            return redirect("dashboard/index")
        else:
            print(form.errors)
    context = {
        "form": AddOrderForm(),
    }
    return render(request, "dashboard/add_order.html", context)