from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('item/<int:id>', views.item, name='item'),
    path('bid/<int:id>', views.bid, name='bid')
]
