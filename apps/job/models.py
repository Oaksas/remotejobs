from django.db import models
from django.contrib.auth.models import User
from .utilities import CHOISE_SIZE, SIZE_1_TO_10, JOB_CATEGORY, CHOISE_JOB_TYPE, JOB_TYPE_FULL_TIME, CHOISE_JOB_STATUS, JOB_STATUS_OPEN, JOB_STATUS_CLOSED
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField(blank=True, null=True)

    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100, blank=True, null=True)
    company_zipcode = models.CharField(
        max_length=100, blank=True, null=True, default='')
    company_country = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.CharField(
        max_length=20, choices=CHOISE_SIZE, blank=True, null=True, default=SIZE_1_TO_10)
    salary = models.CharField(max_length=20, blank=True, null=True)

    category = models.CharField(
        max_length=100, choices=JOB_CATEGORY, blank=True, null=True)

    job_type = models.CharField(max_length=100, choices=CHOISE_JOB_TYPE,
                                blank=True, null=True, default=JOB_TYPE_FULL_TIME)

    job_status = models.CharField(
        max_length=100, choices=CHOISE_JOB_STATUS, blank=True, null=True, default=JOB_STATUS_OPEN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(
        Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['job', 'created_by']

    def __str__(self):
        return self.job.title + ' - ' + self.created_by.username
