from django.contrib import admin
from .models import QuoteRequest


class QuoteRequestAdmin(admin.ModelAdmin):

    readonly_fields = ('request_date',
                       'project_name', 'project_description')

    fields = ('query_closed', 'status', 'company_name', 'full_name',
              'email', 'phone', 'free_consultation_request',
              'project_name', 'project_description', 'request_date', 'notes')

    list_display = ('company_name', 'status', 'full_name',
                    'project_name', 'query_closed')

    ordering = ['request_date']


admin.site.register(QuoteRequest, QuoteRequestAdmin)
