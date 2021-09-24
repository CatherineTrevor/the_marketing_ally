from django.contrib import admin
from .models import QuoteRequest


class QuoteRequestAdmin(admin.ModelAdmin):

    fields = ('company_name', 'full_name',
              'email', 'free_consultation_request',
              'project_name', 'project_description')

    list_display = ('company_name', 'full_name',
              'email', 'free_consultation_request',
              'project_name', 'project_description')

admin.site.register(QuoteRequest)