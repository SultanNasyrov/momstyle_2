from .cart import Cart


def cart(request):
    cart = Cart(request)
    items_number = cart.count_items()
    return {'cart_items_number': items_number}