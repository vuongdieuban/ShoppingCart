from django.shortcuts import render, redirect
from product.models import Product
from .models import Cart
# Create your views here.


def cart_home_view(request):
    template_name = "shoppingcart/cart_home.html"
    obj = Cart.objects.new_or_get(request)
    context = {}
    return render(request, template_name, context)
