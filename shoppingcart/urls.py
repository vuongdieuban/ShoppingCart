from django.urls import path
from .views import cart_home_view, cart_update_view

app_name = 'cart'
urlpatterns = [
    path('', cart_home_view, name='cart-home'),
    path('update/', cart_update_view, name='cart-update')
]
