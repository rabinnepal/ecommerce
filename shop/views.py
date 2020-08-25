from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
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
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        description=request.POST.get("description","")
        contact=Contact(name=name,email=email,phone=phone,description=description)
        contact.save()
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request, "shop/tracker.html")

def search(request):
    return render(request, "shop/search.html")


def productview(request,myid):
    #Fetch the product using id
    productview = Product.objects.filter(id=myid)
    print(productview)
    return render(request, "shop/products.html",{'productview':productview[0]})


def checkout(request):
    return render(request, "shop/checkout.html")