from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_quotes, name='view_quotes'),
    path('quotes/edit/<int:quote_id>', views.edit_quotes, name='edit_quotes'),
]
