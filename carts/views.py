from django.shortcuts import render

from .models import Cart


def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj


def cart_home(request):
    cart_id = request.session.get("get_id", None)
    # if cart_id is None:
    #     cart = cart_create()
    #     request.session['cart_id'] = cart.id
    # else:
    qs = Cart.objects.filter(id=cart_id)
    if qs and qs.count() == 1:
        cart = qs.first()
    else:
        cart = cart_create()
        request.session['cart_id'] = cart.id
    return render(request, 'carts/home.html', {})
