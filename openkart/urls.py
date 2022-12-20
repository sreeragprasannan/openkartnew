from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from core.views import frontpage,shop,signup,login
from product.views import product
from cart.views import add_to_cart

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name= 'add_to_cart'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)