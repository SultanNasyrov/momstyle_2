from django.shortcuts import render, Http404, HttpResponse
from django.views.generic import View
from .cart import Cart

import json


def cart(request):
    cart = Cart(request)
    context = {}
    context['cart_items'] = cart.get_items_list()
    context['total'] = cart.total()
    return render(request, 'cart.html', context)


def add_item(request):

    if request.method =='POST' and request.is_ajax():
        cart = Cart(request)
        product_id, size, quantity = request.POST['product_id'], request.POST['size'], request.POST['quantity']
        cart.add_item(product_id, size, quantity)
        # cart.clean()
        print(cart.cart)
        response = {}
        response['items'] = cart.count_items()
        return HttpResponse(json.dumps(response))
    else:
        raise Http404

def delete_item(request):

    if request.method == 'POST' and request.is_ajax():
        cart = Cart(request)
        key = request.POST['key']
        cart.delete_item(key)
        response = {
        'items': cart.count_items()
        }
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def change_quantity(request):
    if request.method == 'POST' and request.is_ajax():
        cart = Cart(request)
        key, quantity = request.POST['key'], request.POST['quantity']
        cart.change_quantity(key, quantity)
        response = {'total': cart.total(), 'subtotal': cart.cart[key]['subtotal']}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def clean(request):
    if request.method == 'GET' and request.is_ajax():
        cart = Cart(request)
        cart.clean()
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404

def make_order(request):

    if request.method == 'POST' and request.is_ajax():
        name, phone = request.POST['name'], request.POST['phone_number']
        cart = Cart(request)
        cart.make_order(name, phone)
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


