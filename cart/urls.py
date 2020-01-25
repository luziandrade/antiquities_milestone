from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('adjust_cart/<int:id>', views.adjust_cart, name='adjust_cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
