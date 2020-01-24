from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def see_product(request, id):
    product = Product.objects.get(id=id)
    product.save()

    return render(request, "product.html", {'product': product})
