from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('comment',)

    fields = ('comment', 'full_name',
              'email',)

    list_display = ('comment', 'full_name',
              'email',)

admin.site.register(Order)