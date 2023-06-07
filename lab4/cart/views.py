from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Realty
from .cart import Cart
from .forms import CartAddRealtyForm
from django.core.exceptions import PermissionDenied

@require_POST
def cart_add(request, realty_id):
    if not request.user.is_authenticated :
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    realty = get_object_or_404(Realty, id=realty_id)
    form = CartAddRealtyForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(realty=realty,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, realty_id):
    if not request.user.is_authenticated :
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    realty = get_object_or_404(Realty, id=realty_id)
    cart.remove(realty)
    return redirect('cart:cart_detail')


def cart_detail(request):
    if not request.user.is_authenticated :
        raise PermissionDenied("You do not have access to this page.")

    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddRealtyForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
