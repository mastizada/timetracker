from django.db import models


class Customer(models.Model):
    """Customer Details."""
    name = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
