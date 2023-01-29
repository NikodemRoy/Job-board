from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm, widgets

from APPS.profiles.models import WorkerProfile, EmployerProfile

from allauth.account.forms import SignupForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')
        def save(self, request):
            user = super(RegisterForm, self).save(request)
            user.account_type = 'worker'
            user.save()
            return user

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)

class WorkerSignupForm(SignupForm):
    def save(self, request):
        user = super(WorkerSignupForm, self).save(request)
        user.account_type = 'worker'
        profile = WorkerProfile.objects.create(user=user)
        profile.save()
        user.save()
        return user

class EmployerSignupForm(SignupForm):
    def save(self, request):
        user = super(EmployerSignupForm, self).save(request)
        user.account_type = 'employer'
        profile = EmployerProfile.objects.create(user=user)
        profile.save()
        user.save()
        return user