from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from team.models import Team

class User(AbstractUser):
    """
    Custom user
    """
    name = models.CharField(_('name'), max_length=30, blank=False, null=False)
    teams = models.ManyToManyField(Team)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.username and self.email:
            self.username = self.email
        super(User, self).save(*args, **kwargs)


class AuthenticationMethod(SessionAuthentication):
    """
    Ignore CSRF for enabling Token access to api
    """
    def enforce_csrf(self, request):
        # Do not check csrf to be able to login both over web and api
        return


class ApiPagination(PageNumberPagination):
    """
    Pagination params for list results in api
    """
    page_size = 10
    page_size_query_param = 'size'
