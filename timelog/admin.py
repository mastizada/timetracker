from django.contrib import admin
from timelog.models import TimeLog


class TimelogAdmin(admin.ModelAdmin):
    """Timelog in Django Admin."""
    list_display = ('__str__', 'started_at', 'ended_at', )
    list_filter = ('project', 'ended_at', )


admin.site.register(TimeLog, TimelogAdmin)
