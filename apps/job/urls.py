from django.urls import path
from .views import AddJobView, job_detail, ApplyForJobView
urlpatterns = [
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('add/', AddJobView.as_view(), name='add_job'),
    path('apply/<int:job_id>/', ApplyForJobView.as_view(), name='apply_for_job'),


]
