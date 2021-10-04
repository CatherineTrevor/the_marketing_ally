from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'is_available_guest_user'
    )

    readonly_fields = (
        'friendly_name',
        'name',
        'is_available_guest_user'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
