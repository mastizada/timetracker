"""
TimeTracker URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

from timelog import views as timelog_views
from project import views as project_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('rest_auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/users/(?P<pk>\d+)/$', timelog_views.update_timelog, name="user-detail"),
    url(r'^api/customers/(?P<pk>\d+)/$', timelog_views.update_timelog, name="customer-detail"),
    url(r'^api/teams/(?P<pk>\d+)/$', timelog_views.update_timelog, name="team-detail"),
    url(r'^api/projects/$', project_views.list_projects, name="projects-list"),
    url(r'^api/projects/(?P<pk>\d+)/$', project_views.get_project, name="project-detail"),
    url(r'^api/projects/(?P<project_pk>\d+)/timelogs/$', timelog_views.list_timelogs, name="project-timelogs"),
    url(r'^api/projects/(?P<project_pk>\d+)/timelogs/(?P<pk>\d+)/$', timelog_views.get_timelog, name="project-timelog"),
]
