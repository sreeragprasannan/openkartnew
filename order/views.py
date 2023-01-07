from django.shortcuts import render, redirect
import json
from cart.cart import Cart
import stripe
from .models import Order, OrderItem
from django.conf import settings
from django.http import JsonResponse

def start_order(request):
    cart = Cart(request)
    data = json.loads(request.body)
    total_price = 0
    
    items = []
    
    for item in cart:
        product = item['product']
        total_price += product.price * int(item['quantity'])
        
        obj = {
            'price_data':{
                'currency': 'inr',
                'product_data': {
                    'name': product.name,
                },
                'unit_amount': product.price,
            },
            'quantity': item['quantity'],
        }
        
        item.append(obj)
        
    session = ''
    payment_intent = ''
    
    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
    session = stripe.checkout.Session.create(
        pyment_method_types=['card'],
        line_items=items,
        mode='payment',
        success_url='http://127.0.0.1:8000/cart/success/',
        cancel_url='http://127.0.0.1:8000/cart/'
    )
    payment_intent = session.payment_intent
    
    first_name = request.POST.get['first_name']
    last_name = request.POST.get['last_name']
    email = request.POST.get['email']
    address = request.POST.get['address']
    zipcode = request.POST.get['zipcode']
    place = request.POST.get['place']
    phone = request.POST.get['phone']

    order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, zipcode=zipcode, place=place)
    order.payment_intent = payment_intent
    oder.paid_amount = total_price
    oder.paid = True
    order.save()
    

    for item in cart:
        product = item['product']
        quantity = int(item['quantity'])
        price = product.price * quantity

        item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)


    return JsonResponse({'session': session, 'order': payment_intent})