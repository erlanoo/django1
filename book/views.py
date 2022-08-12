from django.shortcuts import render, HttpResponse, get_object_or_404
from . import models


def homepage(request):
    queryset = models.Product.objects.all()
    return render(request, "book/homepage.html", {"product": queryset})


def categories_view(request):
    categories = models.Category.objects.all()
    c = {"categories": categories}
    return render(request, "book/categories.html", c)


def category_detail(request, id):
    # SELECT = FROM Product WHERE category = (SELECT id FROM Category WHERE id = id)
    category_object = models.Category.objects.get(id=id)
    product_list = models.Product.objects.filter(category=category_object)
    context = {"all_product": product_list}
    return render(request, 'book/product_list.html', context)


def product_detail(request, id):
     prod = get_object_or_404(models.Product,id=id)
     return render(request,"book/product_detail.html",{'product':prod})



def about_view(request):
    return render(request, "about.html")


def product_view(request):
    product_object = models.Product.objects.order_by('id')
    return render(request, "book/product_list.html",{'product_list':product_object})
