"""ekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views
from django.conf import settings
from django.conf.urls.static import static
from book.views import category_detail, product_detail, categories_view, sig_in, homepage
from book.views import price_view, PricingDetailView, PricingListViesw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('categories/', categories_view, name='Category_list'),
    path('categories/<int:id>/', category_detail, name='Category_detail'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('about/', views.about_view, name='about'),
    path('price/', price_view, name="price"),
    path('product/', views.product_view, name="product"),
    path('sigin/', sig_in, name="register"),
    path('pricing/', PricingListViesw.as_view()),
    path('pricing/<int:id>/', PricingDetailView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)