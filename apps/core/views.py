from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

from apps.job.models import Job
from apps.userprofile.models import UserProfile


def frontpage(request):
    jobs = Job.objects.all().order_by('-created_at')[:3]
    return render(request, 'core/frontPage.html', {'jobs': jobs})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            user = form.save()
            account_type = request.POST.get('account_type', 'jobseeker')
            if account_type == 'employer':

                userprofile = UserProfile.objects.create(
                    user=user, is_employer=True)
                print(userprofile)
                userprofile.save()
            else:
                userprofile = UserProfile.objects.create(
                    user=user, is_employer=False)
                userprofile.save()
            login(request, user)
            # Redirect to the home page
            return redirect('dashboard')
    form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})
