from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

from apps.job.models import Job


def frontpage(request):
    jobs = Job.objects.all()[0:3]
    return render(request, 'core/frontPage.html', {'jobs': jobs})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Save the new user to the database
            user = form.save()
            login(request, user)
            # Redirect to the home page
            return redirect('frontpage')
    form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})
