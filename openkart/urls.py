from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib.auth import views
from core.views import frontpage,shop,signup
from product.views import product
from cart.views import add_to_cart
from openkart import settings

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html') , name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name= 'add_to_cart'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)