from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.urls import reverse
from timelog.models import TimeLog


class TimelogAdmin(admin.ModelAdmin):
    """Timelog in Django Admin."""
    list_display = ('__str__', 'started_at', 'ended_at', 'duration', 'associated_user', 'associated_project', )
    list_filter = ('project', 'ended_at', 'user', )

    def associated_project(self, obj):
        return '<a href="{url}?id={pk}">{name}</a>'.format(
            url=reverse('admin:project_project_changelist'),
            pk=obj.project.pk,
            name=obj.project
        )

    def associated_user(self, obj):
        return '<a href="{url}?id={pk}">{name}</a>'.format(
            url=reverse('admin:common_user_changelist'),
            pk=obj.user.pk,
            name=obj.user
        )

    associated_project.allow_tags = True
    associated_project.short_description = _("Project")
    associated_user.allow_tags = True
    associated_user.short_description = _("User")


admin.site.register(TimeLog, TimelogAdmin)
