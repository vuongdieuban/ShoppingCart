from django.urls import path
from .views import cart_home_view

app_name = 'cart'
urlpatterns = [
    path('', cart_home_view, name='cart-home'),
]
