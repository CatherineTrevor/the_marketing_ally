from django.urls import path
from . import views


urlpatterns = [
    path('', views.order_basket, name='order_basket'),
    path('calendar/', views.calendar, name='calendar'),
    path('bag/', views.view_bag, name='view_bag'),
    path('add/<product_id>', views.add_to_bag, name='add_to_bag'),
    path('remove/<item_id>',
         views.remove_from_bag, name='remove_from_bag'),
    path('update/<item_id>',
         views.add_timeslot_note, name='add_timeslot_note'),
]
