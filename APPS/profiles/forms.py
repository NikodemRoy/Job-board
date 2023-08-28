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