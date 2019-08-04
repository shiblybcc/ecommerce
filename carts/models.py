from django.db import models
from django.conf import settings

from products.models import Product

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):

    def new_or_get(self, request):
        cart_id = request.session.get("get_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs and qs.count() == 1:
            new_cart = False
            cart = qs.first()
            if request.user.is_authenticated() and cart.user is None:
                cart.user = request.user
                cart.save()
        else:
            cart = Cart.objects.new(user=request.user)
            new_cart = True
            request.session['cart_id'] = cart.id
        return cart, new_cart

    def new(self, user=None):
        new_user = None
        if user is not None:
            if user.is_authenticated:
                new_user = user
        return self.model.objects.create(user=new_user)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.0, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)
