from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_received/<id>',
         views.contact_received,
         name='contact_received'),
]
