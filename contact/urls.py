from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact_success/<quote_request_id>',
         views.contact,
         name='contact_success'),    
]
