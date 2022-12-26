from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from itertools import product
# Create your models here.
class Order(models.Model):
    ORDERED = 'odered'
    SHIPPED = 'shipped'
    
    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )
    
    user = models.ForeignKey(User,related_name='order', blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items' ,on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)