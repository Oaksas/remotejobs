from django import forms
from .models import Job, Application


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['created_at', 'updated_at', 'created_by']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']
