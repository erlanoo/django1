from django.shortcuts import render, HttpResponse, get_object_or_404
from . import models
from .models import Category


def homepage(request):
    queryset = models.Product.objects.all()
    return render(request, "book/homepage.html", {"product": queryset})


def categories_view(request):
    categories = models.Category.objects.all()
    c = {"categories": categories}
    return render(request, "book/categories.html", c)


def category_detail(request, id):
    category = Category.objects.get(id=id)
    context = {"Category": category}
    return render(request, "book/category_detail.html", context)

def product_detail(request, id):
     prod = get_object_or_404(models.Product,id=id)
     return render(request,"book/product_detail.html",{'product':prod})


def about_view(request):
    return render(request, "about.html")


def product_view(request):
    product_object = models.Product.objects.order_by('id')
    return render(request, "book/product_list.html",{'product_list':product_object})
