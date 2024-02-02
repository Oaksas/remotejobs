from django.urls import path
from .views import AddJobView, job_detail, ApplyForJobView, get_all_jobs, EditJobView
urlpatterns = [
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('add/', AddJobView.as_view(), name='add_job'),
    path('<int:job_id>/edit/', EditJobView.as_view(), name='edit_job'),
    path('apply/<int:job_id>/', ApplyForJobView.as_view(), name='apply_for_job'),
    path('all/', get_all_jobs, name='all_jobs')


]
