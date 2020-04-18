from django.urls import path, include 
from . import views
from django.conf.urls import url
from django.views.generic import ListView , DetailView
from . models import Product

urlpatterns = [
	path('', ListView.as_view(queryset=Product.objects.all(), template_name="shop/shop.html")),
	path('<int:pk>/', DetailView.as_view(model=Product, template_name="shop/product.html")),
]