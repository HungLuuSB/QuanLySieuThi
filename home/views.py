from django.shortcuts import render, get_object_or_404, redirect
from common.models.product import Product
from common.models.category import Category
from .forms import ProductForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def product_list(request):
    category_id = request.GET.get('category')
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home/product_list.html', {'products': products, 'categories': categories})

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'home/product_form.html', {'form': form, 'title': 'Thêm sản phẩm'})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form = ProductForm(request.POST, request.FILES, instance=product)
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'home/product_form.html', {'form': form, 'title': 'Sửa sản phẩm'})

def product_delete(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
    return redirect('product_list')



