from django.urls import path
from . import views


urlpatterns = [
    path('', views.order_basket, name='order_basket'),
    path('calendar/', views.calendar, name='calendar'),
    path('bag/', views.view_bag, name='view_bag'),
    path('add_to_bag/<product_id>', views.add_to_bag, name='add_to_bag'),
]
