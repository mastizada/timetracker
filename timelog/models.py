from django.db import models
from project.models import Project

class TimeLog(models.Model):
    """
    Time Logger
    """
    started_at = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    ended_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name='timelogs', null=False, blank=False)

    def __str__(self):
        return self.project.__str__() + ' ' + str(self.started_at)

    def save(self, *args, **kwargs):
        if self.started_at and self.ended_at:
            self.duration = round((self.ended_at - self.started_at).seconds / 60)
        super(TimeLog, self).save(*args, **kwargs)
