from django.contrib import admin
from timelog.models import TimeLog


class TimelogAdmin(admin.ModelAdmin):
    """Timelog in Django Admin."""
    pass


admin.site.register(TimeLog, TimelogAdmin)
