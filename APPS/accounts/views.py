from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm
from .models import EmployerProfile

def login_page(request):
    return render(request, 'accounts/login.html')


def employer_registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.account_type = 'employer'
            user.save()

            # Create user profile
            profile = EmployerProfile.objects.create(user=user)
            profile.save()

            messages.success(request, 'Account created succesfull!')
            # login(request, user)
            return redirect('index_page')
        else:
            # messages.error(request, "Email or password is incorect!")
            return redirect('index_page')

    context = {'employer_form':form}
    return render(request, "job_board/main_index.html", context)


def worker_registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.account_type = 'worker'
            user.save()

            # Create user profile
            profile = EmployerProfile.objects.create(user=user)
            profile.save()

            messages.success(request, 'Account created succesfull!')
            # login(request, user)
            return redirect('index_page')
        else:
            # messages.error(request, "Email or password is incorect!")
            return redirect('index_page')

    context = {'employer_form':form}
    return render(request, "job_board/main_index.html", context)
