from django.shortcuts import render, redirect

from products.models import Product
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(request, "carts/home.html", {})


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