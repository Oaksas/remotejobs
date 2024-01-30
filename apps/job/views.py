from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Job
from .forms import AddJobForm, ApplicationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, FormView

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


@method_decorator(login_required, name='dispatch')
class ApplyForJobView(FormView, DetailView):
    template_name = 'job/apply_for_job.html'
    form_class = ApplicationForm
    model = Job
    context_object_name = 'job'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        job = self.get_object()
        application = form.save(commit=False)
        application.job = job
        application.created_by = self.request.user
        application.save()
        return redirect('dashboard')

    def get_object(self, queryset=None):
        job_id = self.kwargs.get('job_id')
        return Job.objects.get(pk=job_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
