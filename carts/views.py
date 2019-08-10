from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {'cart': cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect('cart:home')
        cart, new_cart = Cart.objects.new_or_get(request)
        if product in cart.products.all():
            cart.products.remove(product)
        else:
            cart.products.add(product)

    return redirect("cart:home")