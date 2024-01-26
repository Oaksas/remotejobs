from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Job
from .forms import AddJobForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'job/job_detail.html', {'job': job})


@method_decorator(login_required, name='dispatch')
class AddJobView(CreateView):
    model = Job
    form_class = AddJobForm
    template_name = 'job/add_job.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
