from django.shortcuts import render

from .models import Cart


def cart_home(request):
    cart_id = request.session.get("get_id", None)
    qs = Cart.objects.filter(id=cart_id)
    if qs and qs.count() == 1:
        cart = qs.first()
        if request.user.is_authenticated() and cart.user is None:
            cart.user = request.user
            cart.save()
    else:
        cart = Cart.objects.new(user=request.user)
        request.session['cart_id'] = cart.id
    return render(request, 'carts/home.html', {})
