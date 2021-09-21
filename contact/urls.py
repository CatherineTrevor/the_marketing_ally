from django.urls import path
from . import views

urlpatterns = [
    path('get_in_touch/', views.contact, name='contact')
]
