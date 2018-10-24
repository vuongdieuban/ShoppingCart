from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product
# Create your views here.


def product_list_view(request):
    template_name = 'product/product_list.html'
    query_set = Product.objects.all()
    context = {
        "object_list": query_set,
    }
    return render(request, template_name, context)
