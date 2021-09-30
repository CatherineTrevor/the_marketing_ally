from django.contrib import admin
from .models import OrderRequest


class OrderRequestAdmin(admin.ModelAdmin):

    readonly_fields = ('id', 'account_company_name', 'timeslot_option_1',
                       'timeslot_option_2', 'project_name',
                       'project_description', 'is_digital')

    fields = ('id', 'account_company_name', 'timeslot_option_1',
              'timeslot_option_2', 'project_name', 'project_description',
              'is_digital', 'total_booking_hours', 'total_order_value',
              'order_status', 'order_timeslot_confirmed')

    list_display = ('id', 'account_company_name', 'order_status',
                    'order_timeslot_confirmed')


admin.site.register(OrderRequest, OrderRequestAdmin)
