from django.urls import path
from .views import product_list_view

app_name = 'product'
urlpatterns = [
    path('', product_list_view, name='product-list'),
]
