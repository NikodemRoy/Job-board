from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm, widgets

from allauth.account.forms import SignupForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)

class EmployeeSignupForm(SignupForm):
    def save(self, request):
        user = super(EmployeeSignupForm, self).save(request)
        user.account_type = 'worker'
        user.save()
        return user