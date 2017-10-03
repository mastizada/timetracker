from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.db.models import Sum
from django.urls import reverse
from common.models import User
from timelog.models import TimeLog
from team.models import Team
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    """Custom user in Django Admin."""
    list_display = ('pk', '__str__', 'email', 'teamlist', 'work_hours', 'modified_at',)
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

    def teamlist(self, obj):
        teams = []
        for team in obj.teams.all():
            teams.append(
                '<a href="{url}">{name}</a>'.format(
                    url=reverse('admin:team_team_change', args=(team.pk,)),
                    name=team.name
                )
            )
        return ','.join(teams)

    def work_hours(self, obj):
        hours = TimeLog.objects.filter(user=obj).aggregate(Sum('duration'))['duration__sum']
        if not hours:
            return "0 hours"
        return "{:.2f} hours".format(hours / 60.0)  # @TODO L10n

    teamlist.allow_tags = True
    teamlist.short_description = _("Teams")


admin.site.register(User, CustomUserAdmin)
