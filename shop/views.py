from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    allProducts = []
    catProds = Product.objects.values("category", "id")
    cats = {item["category"] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProducts.append([prod, range(1, nSlides), nSlides])
    # params = {"noOfSlide": nSlides, "range": range(1, nSlides), "product": products}
    # allProducts = [
    #     [products, range(1, nSlides), nSlides],
    #     [products, range(1, nSlides), nSlides],
    # ]
    params = {"allProducts": allProducts}
    return render(request, "shop/index.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    return HttpResponse("We are in contact section")


def tracker(request):
    return HttpResponse("We are in tracker section")


def search(request):
    return HttpResponse("We are in search section")


def productview(request):
    return HttpResponse("We are in productview section")


def checkout(request):
    return HttpResponse("We are in checkout section")
