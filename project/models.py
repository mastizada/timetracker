from django.db import models
from customer.models import Customer

class Project(models.Model):
    """
    Project information
    """
    name = models.CharField(max_length=254, blank=False, null=False)
    customer = models.ForeignKey(Customer, related_name='projects', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
