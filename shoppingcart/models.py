from django.db import models
from django.conf import settings
from product.models import Product
# Create your models here.

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    # create new cart for a session. If user is authenticated then associate the cart to the user
    def new_cart(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

    # Handle the logic of the cart exist or not
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        print("existing cart_id is ", cart_id)

        # if don't have a cart_id then we create a new cart_obj, assign the new cart obj's id to the session key "cart_id"
        if cart_id is None:
            cart_obj = self.new_cart(user=request.user)
            request.session["cart_id"] = cart_obj.id
            print("new cart id created, new id is", request.session["cart_id"])

        # if we do have a cart id then assign it to the cart obj. If the user is then log in, we associate the cart to the user
        else:
            queryset = self.get_queryset().filter(id=cart_id)
            cart_obj = queryset.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        return cart_obj


class Cart(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'

    # override the objects attribute since we are using a self defining CartManager class to create new objects
    objects = CartManager()
