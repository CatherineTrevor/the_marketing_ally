from django.contrib import admin
from .models import QuoteRequest


class QuoteRequestAdmin(admin.ModelAdmin):

    readonly_fields =('quote_request_id', 'company_name', 'full_name',
              'email', 'free_consultation_request',
              'project_name', 'project_description')

    fields = ('quote_request_id', 'consultation_status', 'company_name', 'full_name',
              'email', 'free_consultation_request',
              'project_name', 'project_description')

    list_display = ('quote_request_id', 'consultation_status', 'company_name', 'full_name',
              'project_name',)


admin.site.register(QuoteRequest, QuoteRequestAdmin)