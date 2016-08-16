from django.contrib import admin
from project.models import Project


class ProjectAdmin(admin.ModelAdmin):
    """Project in Django Admin."""
    pass


admin.site.register(Project, ProjectAdmin)
