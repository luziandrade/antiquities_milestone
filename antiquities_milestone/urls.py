from django.contrib import admin
from django.urls import path, include, re_path
from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('search/', include('search.urls')),
    path('checkout/', include('checkout.urls')),
    path('bids/', include('bidding.urls')),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
