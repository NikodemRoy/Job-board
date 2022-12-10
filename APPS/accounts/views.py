from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from allauth.account.views import SignupView

from .forms import RegisterForm, WorkerSignupForm, EmployerSignupForm
from .models import EmployerProfile

def login_page(request):
    return render(request, 'accounts/login.html')

# Employee Signup View
class EmployerSignupView(SignupView):

    template_name = 'accounts/signup_employer.html'  # Custom template is mandatory
    form_class = EmployerSignupForm
    redirect_field_name = 'next'  # Important to redirect user if has next url

    # This is mandatory and copy-pasted
    # def get_context_data(self, **kwargs):
    #     ret = super(EmployerSignupForm, self).get_context_data(**kwargs)
    #     ret.update(self.kwargs)
    #     return ret

# Employee Signup View
class WorkerSignupView(SignupView):

    template_name = 'accounts/signup_worker.html'  # Custom template is mandatory
    form_class = WorkerSignupForm
    redirect_field_name = 'next'  # Important to redirect user if has next url

    # This is mandatory and copy-pasted
    # def get_context_data(self, **kwargs):
    #     ret = super(WorkerSignupForm, self).get_context_data(**kwargs)
    #     ret.update(self.kwargs)
    #     return ret


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def employer_registration(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.email = user.email.lower()
#             user.account_type = 'employer'
#             user.save()

#             # Create user profile
#             profile = EmployerProfile.objects.create(user=user)
#             profile.save()

#             messages.success(request, 'Account created succesfull!')
#             # login(request, user)
#             return redirect('index_page')
#         else:
#             # messages.error(request, "Email or password is incorect!")
#             return redirect('index_page')

#     context = {'employer_form':form}
#     return render(request, "job_board/main_index.html", context)


# def worker_registration(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.email = user.email.lower()
#             user.account_type = 'worker'
#             user.save()

#             # Create user profile
#             profile = EmployerProfile.objects.create(user=user)
#             profile.save()

#             messages.success(request, 'Account created succesfull!')
#             # login(request, user)
#             return redirect('index_page')
#         else:
#             # messages.error(request, "Email or password is incorect!")
#             return redirect('index_page')

#     context = {'employer_form':form}
#     return render(request, "job_board/main_index.html", context)

