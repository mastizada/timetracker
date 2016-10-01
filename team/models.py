from django.db import models

class Team(models.Model):
    """
    Team information
    """
    name = models.CharField(max_length=254, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
