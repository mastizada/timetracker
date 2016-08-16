from django.contrib import admin
from customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    """Customer in Django Admin."""
    pass


admin.site.register(Customer, CustomerAdmin)
