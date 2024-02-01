from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.notification.utilities import createNotification
from apps.notification.models import Notification
from .models import Job
from apps.job.models import Application
from .forms import AddJobForm, ApplicationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, FormView
from .utilities import countries


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['countries'] = countries

        return context


@method_decorator(login_required, name='dispatch')
class ApplyForJobView(FormView, DetailView):
    template_name = 'job/apply_for_job.html'
    form_class = ApplicationForm
    model = Job
    context_object_name = 'job'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        has_applied = self.has_user_applied(self.object)
        print('-----------------------------------------------')
        print(has_applied)
        context = self.get_context_data(
            form=self.get_form(), has_applied=has_applied)
        return self.render_to_response(context)

    def has_user_applied(self, job):
        user = self.request.user
        return Application.objects.filter(job=job, created_by=user).exists()

    def form_valid(self, form):
        job = self.get_object()
        application = form.save(commit=False)
        application.job = job
        application.created_by = self.request.user
        application.save()

        createNotification(self.request, to_user=job.created_by,
                           notification_type=Notification.APPLICATION, extra_id=application.id)
        return redirect('dashboard')

    def get_object(self, queryset=None):
        job_id = self.kwargs.get('job_id')
        return Job.objects.get(pk=job_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


def get_all_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'job/all_jobs.html', {'jobs': jobs})
