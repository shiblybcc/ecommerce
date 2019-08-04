from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed

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
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    instance.total = instance.subtotal  + 10 #* 1.08


pre_save.connect(pre_save_cart_receiver, sender=Cart)

