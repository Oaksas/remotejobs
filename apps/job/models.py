from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
