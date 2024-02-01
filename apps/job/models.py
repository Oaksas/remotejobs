from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Job(models.Model):
    SIZE_1_TO_10 = 'size_1-10'
    SIZE_11_TO_50 = 'size_11-50'
    SIZE_51_TO_200 = 'size_51-200'
    SIZE_201_TO_500 = 'size_201-500'

    CHOISE_SIZE = (
        (SIZE_1_TO_10, '1-10'),
        (SIZE_11_TO_50, '11-50'),
        (SIZE_51_TO_200, '51-200'),
        (SIZE_201_TO_500, '201-500'),
    )

    title = models.CharField(max_length=100)
    short_description = models.TextField()
    long_description = models.TextField(blank=True, null=True)

    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100, blank=True, null=True)
    company_zipcode = models.CharField(max_length=100, blank=True, null=True)
    company_country = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.CharField(
        max_length=20, choices=CHOISE_SIZE, blank=True, null=True, default=SIZE_1_TO_10)
    salary = models.IntegerField(null=True)

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
