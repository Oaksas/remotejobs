from django.urls import path
from .views import AddJobView, job_detail
urlpatterns = [
    path('<int:job_id>/', job_detail, name='job_detail'),
    path('add/', AddJobView.as_view(), name='add_job'),


]
