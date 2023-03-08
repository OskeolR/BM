"""BMProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from MaleApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', views.index),
    re_path(r'^$',views.index, name='index'),
    path('index/', views.index, name='index'),
    path('men/', views.men, name='men'),
    path('female/', views.female, name='female'),
    path('products/', views.products, name='products'),
    path('products_female/', views.products_female, name='products_female'),
    path('product_male/', views.product_male, name='product_male'),
    path('product_female/', views.product_female, name='product_female'),
    path('form/', views.form, name='form'),
    path('payment/', views.payment, name='payment'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('success/', views.success, name='success'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('search/', views.search, name='search'),
    path('profil/', views.profil, name='profil'),
    path('create_order/', views.create_order, name='create_order'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)