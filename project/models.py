from django.db import models
from customer.models import Customer
from team.models import Team

class Project(models.Model):
    """
    Project information
    """
    name = models.CharField(max_length=254, blank=False, null=False)
    customer = models.ForeignKey(
        Customer,
        related_name='projects',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )
    rate = models.DecimalField(
        verbose_name="Hourly Rate",
        max_digits=25,
        decimal_places=2,
        default=0
    )
    team = models.ForeignKey(
        Team,
        related_name='projects',
        blank=False, null=False,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
