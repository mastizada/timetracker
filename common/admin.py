from django.contrib import admin
from common.models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    """Custom user in Django Admin."""
    list_display = ('pk', '__str__', 'email', 'modified_at',)
    list_filter = ('teams', )
    fieldsets = (
        ('Account Info', {
            'fields': ('name', 'username', 'email', 'groups', 'is_staff', 'is_active',)
        }),
        ('Extra Details', {
            'fields': ('teams',)
        }),
        ('Password', {
            'fields': ('password',)
        }),
    )


admin.site.register(User, CustomUserAdmin)
