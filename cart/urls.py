from cart.views import add_to_cart,cart,checkout
from django.urls import path,include

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name= 'add_to_cart'),
]
