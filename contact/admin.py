from django.contrib import admin
from .models import QuoteRequest


class QuoteRequestAdmin(admin.ModelAdmin):

    readonly_fields = ('email', 'free_consultation_request',
              'project_name', 'project_description')

    fields = ('consultation_status', 'company_name', 'full_name',
              'email', 'phone', 'free_consultation_request',
              'project_name', 'project_description', 'notes')

    list_display = ('company_name', 'consultation_status', 'full_name',
              'project_name',)

    ordering = ['full_name']


admin.site.register(QuoteRequest, QuoteRequestAdmin)
