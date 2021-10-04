from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_confirmation/', views.checkout_confirmation, name='checkout_confirmation'),    
]
