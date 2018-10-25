from django.shortcuts import render, redirect
from django.urls import reverse
from product.models import Product
from .models import Cart
# Create your views here.


def cart_home_view(request):
    template_name = "shoppingcart/cart_home.html"
    cart_obj = Cart.objects.new_or_get(request)
    cart_products = cart_obj.products.all()
    total_price = 0
    for product in cart_products:
        total_price = total_price + product.price
    cart_obj.total = total_price
    cart_obj.save()
    context = {
        "cart": cart_obj,
    }
    return render(request, template_name, context)


def cart_update_view(request):
    product_id = request.POST.get('product_id')
    product_obj = Product.objects.get(id=product_id)
    cart_obj = Cart.objects.new_or_get(request)

    # cart_obj.products.add(product_obj)  # add data into ManytoMany field
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    # return render(request, template_name, context)
    return redirect("cart:cart-home")
