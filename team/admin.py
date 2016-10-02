from django.contrib import admin
from team.models import Team


class TeamAdmin(admin.ModelAdmin):
    """Teams in Django Admin."""
    pass


admin.site.register(Team, TeamAdmin)
