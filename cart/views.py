from django.shortcuts import render
from .cart import Cart
from django.contrib.auth.decorators import login_required 

# Create your views here.
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    
    return render(request, 'cart/menu_cart.html')

def cart(request):
    return render(request, 'cart/cart.html')

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')