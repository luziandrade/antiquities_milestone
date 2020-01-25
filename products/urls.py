from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:id>', views.see_product, name='see_product')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
