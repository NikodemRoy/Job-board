from django import forms
from .models import JobOffer

class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = ('title', 'description', 'city', 'post_code', 'addres', 'job_type', 'category',
         'experience', 'salary', 'monthly_working_hours' 'currency')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add Job Tile'}),
            'description': forms.Textarea(attrs={'placeholder': 'Here you can add a description of the job posting','rows':'4'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Add Your Phone Number'}),
            'languages': forms.TextInput(attrs={'placeholder': 'Add Your Languages'}),
            'job_title': forms.TextInput(attrs={'placeholder': 'Add Your Job Title'}),
            'country': forms.TextInput(attrs={'placeholder': 'e.x Poland'}),
            'city': forms.TextInput(attrs={'placeholder': 'e.x Warsaw'}),
            'fb_link': forms.TextInput(attrs={'placeholder': 'https://www.facebook.com/'}),
            'twitter_link': forms.TextInput(attrs={'placeholder': 'https://twitter.com/'}),
            'linkedin_link': forms.TextInput(attrs={'placeholder': 'https://in.linkedin.com/'}),
            'instagram_link': forms.TextInput(attrs={'placeholder': 'https://www.instagram.com/'}),
            'youtube_link': forms.TextInput(attrs={'placeholder': 'https://www.youtube.com/'}),
        }
    def __init__(self, *args, **kwargs):
        super(JobOffer, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'