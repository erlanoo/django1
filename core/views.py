from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from core import models
from .form import SiginInForms
from django.contrib.auth import authenticate,login
# Create your views here.
def price_view(request):
    return render(request, "core/price.html")



def sigin_in(request):
    if request.method == 'POST':
        auth_form = SiginInForms(request.POST)
        if auth_form.is_valid():
            user = authenticate(
                request,
                user=auth_form.valdated_data['username'],
                password=auth_form.valdated_data['password']
            )
            if user is not None:
                login(request,user)
                return redirect('homepage')

    context = {'auth_form':SiginInForms()}
    return render(request,'core/sign_in.html', context)

class PricingListViesw(generic.ListView):
    template_name = "core/pricing.html"
    queryset = models.Pricing.objects.order_by("-id")

    def get_queryset(self):
        return self.queryset

class PricingDetailView(generic.DetailView):
    template_name = "core/pricing_detail.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.Pricing, id=show_id)
