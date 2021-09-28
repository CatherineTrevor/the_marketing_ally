from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_basket, name='order_basket'),
]
