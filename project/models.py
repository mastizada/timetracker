from django.db import models
from customer.models import Customer

class Project(models.Model):
    """
    Project information
    """
    name = models.CharField(max_length=254, blank=False, null=False)
    customer = models.ForeignKey(Customer, related_name='projects',
                                 blank=True, null=True)
    rate = models.DecimalField(verbose_name="Hourly Rate", max_digits=25,
                               decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
