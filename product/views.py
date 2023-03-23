from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Review


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')
        
        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)
            
            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
                
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by=request.user
                )
            return redirect('product', slug=slug)

    return render(request, 'product/product.html', {'product': product})


# @login_required
# def add_products(request,):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         category_name = request.POST.get('category')
#         category = Category.objects.create(name=category_name)
#         price = request.POST.get('price')
#         description = request.POST.get('description')
#         image = request.FILES['upload']
        

#         p = Product(name=name,category=category,price=price,description=description,image=image)
#         # p.seller_name = request.user
#         p.save()
        
#         return redirect('/product/products',)

#     return render(request, 'product/addproducts.html', context)