from django import forms
from .models import WorkerProfile, EmployerProfile

from django.forms import ValidationError

class WorkerProfileForm(forms.ModelForm):
    class Meta:
        model = WorkerProfile
        fields = ('name', 'surname', 'phone_number', 'languages', 'job_title', 'country', 'city',
         'profile_description', 'fb_link', 'twitter_link', 'linkedin_link', 'instagram_link', 'youtube_link', )
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Add Your Name'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Add Your Surname'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Add Your Phone Number'}),
            'languages': forms.TextInput(attrs={'placeholder': 'Add Your Languages'}),
            'job_title': forms.TextInput(attrs={'placeholder': 'Add Your Job Title'}),
            'country': forms.TextInput(attrs={'placeholder': 'e.x Poland'}),
            'city': forms.TextInput(attrs={'placeholder': 'e.x Warsaw'}),
            'profile_description': forms.Textarea(attrs={'placeholder': 'Here you can add a brief description of yourself and what you do professionally.','rows':'4'}),
            'fb_link': forms.TextInput(attrs={'placeholder': 'https://www.facebook.com/'}),
            'twitter_link': forms.TextInput(attrs={'placeholder': 'https://twitter.com/'}),
            'linkedin_link': forms.TextInput(attrs={'placeholder': 'https://in.linkedin.com/'}),
            'instagram_link': forms.TextInput(attrs={'placeholder': 'https://www.instagram.com/'}),
            'youtube_link': forms.TextInput(attrs={'placeholder': 'https://www.youtube.com/'}),
        }
    def __init__(self, *args, **kwargs):
        super(WorkerProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ('brand_name', 'country', 'city', 'post_code', 'street', 'phone_number', 'number_of_workers', 'contact_email', 'website',
         'company_description', 'fb_link', 'twitter_link', 'linkedin_link', 'instagram_link', 'youtube_link', )
        widgets = {
            'brand_name': forms.TextInput(attrs={'placeholder': 'Add Your Brand Name'}),
            'country': forms.TextInput(attrs={'placeholder': 'Add Your Country'}),
            'city': forms.TextInput(attrs={'placeholder': 'Add Your Country'}),
            'post_code': forms.TextInput(attrs={'placeholder': 'Add Your Country'}),
            'street': forms.TextInput(attrs={'placeholder': 'Add Your Country'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Add Your Phone Number'}),
            'number_of_workers': forms.NumberInput(attrs={'placeholder': 'Add Your Languages'}),
            'contact_email': forms.TextInput(attrs={'placeholder': 'Add Your Job Title'}),
            'website': forms.TextInput(attrs={'placeholder': 'e.x Poland'}),
            'company_description': forms.Textarea(attrs={'placeholder': 'Here you can add a brief description of your company.','rows':'4'}),
            'fb_link': forms.TextInput(attrs={'placeholder': 'https://www.facebook.com/'}),
            'twitter_link': forms.TextInput(attrs={'placeholder': 'https://twitter.com/'}),
            'linkedin_link': forms.TextInput(attrs={'placeholder': 'https://in.linkedin.com/'}),
            'instagram_link': forms.TextInput(attrs={'placeholder': 'https://www.instagram.com/'}),
            'youtube_link': forms.TextInput(attrs={'placeholder': 'https://www.youtube.com/'}),
        }
    def __init__(self, *args, **kwargs):
        super(EmployerProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'