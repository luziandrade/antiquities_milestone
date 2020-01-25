from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_items, name='items'),
    path('item/<int:id>', views.item, name='item'),
    path('bid/<int:id>', views.edit_bid, name='bid')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
