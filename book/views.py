from django.shortcuts import render, HttpResponse
from . import models
import portfolio
# Create your views here.
def homepage(request):
    queryset = models.Product.objects.all()
    return render(request, "product_list.html", {"product": queryset})

def categories_view(request):
    categories = models.Category.objects.all()
    c = {"categories": categories}
    return render(request, "categories.html", c)


