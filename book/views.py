from django.shortcuts import render, HttpResponse
from . import models
import portfolio
# Create your views here.
def homepage(request):
    queryset = models.Product.objects.all()
    return render(request, "book/product_list.html", {"product": queryset})

def categories_view(request):
    categories = models.Category.objects.all()
    c = {"categories": categories}
    return render(request, "book/categories.html", c)

def about_view(request):
    return render(request, "book/about.html")
