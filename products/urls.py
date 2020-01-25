from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('product/<int:id>', views.see_product, name='see_product')
]
