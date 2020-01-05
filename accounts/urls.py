from django.urls import path, include
from accounts import urls_reset
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('register/', views.registration, name='registration'),
    path('profile/', views.user_profile, name='profile'),
    path('password-reset/', include(urls_reset))
]
