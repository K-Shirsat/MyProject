"""
URL configuration for Dproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='Home'),
    path('product/', views.product, name='Product'),
    path('customer/<str:pk_test>/', views.customer, name='Customers'),
    path('create_order/', views.createOrder, name='Create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='Update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='Delete_order'),
]
