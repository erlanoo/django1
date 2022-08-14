from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic

from . import models
from .models import Category
from .form import RegistrationForm

def homepage(request):
    queryset = models.Product.objects.all()
    return render(request, "homepage.html", {"product": queryset})


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
    return render(request, "book/product_list.html", {'product_list': product_object})


def sig_in(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'book/regist_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request, 'book/register.html', {'user_form': user_form})


class PricingListViesw(generic.ListView):
    template_name = "book/pricing.html"
    queryset = models.Pricing.objects.order_by("id")

    def get_queryset(self):
        return self.queryset

class PricingDetailView(generic.DetailView):
    template_name = "book/pricing_detail.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Pricing, id=show_id)

@login_required(login_url='http://127.0.0.1:8000/sigin')
def price_view(request):
    return render(request, "book/price.html")