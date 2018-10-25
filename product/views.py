from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product
from shoppingcart.models import Cart
# Create your views here.


def product_list_view(request):
    template_name = 'product/product_list.html'
    query_set = Product.objects.all()
    cart_obj = Cart.objects.new_or_get(request)
    context = {
        "product_list": query_set,
        'cart': cart_obj,
    }
    return render(request, template_name, context)
