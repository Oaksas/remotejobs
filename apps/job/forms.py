from django import forms
from .models import Job


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['created_at', 'updated_at', 'created_by']
