from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
]