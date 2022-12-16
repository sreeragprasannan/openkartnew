from django.shortcuts import render
from product.models import Product, Category
# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:8]
    
    return render(request, 'core/frontpage.html', {'products': products})

def shop(request):
    catagories = Category.objects.all()
    products = Product.objects.all()
    
    active_catagory = request.GET.get('catagory', '')
    context ={
        'catagories': catagories,
        'products': products,
        'active_catagory':active_catagory,
    }
        
    return render(request, 'core/shop.html', context)
    