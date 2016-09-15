"""
TimeTracker URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from common.views import UserViewSet
from customer.views import CustomerViewSet
from project.views import ProjectViewSet
from timelog.views import TimeLogViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'timelogs', TimeLogViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
