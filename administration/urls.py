from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_quotes, name='view_quotes'),   
]
