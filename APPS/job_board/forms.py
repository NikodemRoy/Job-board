from django import forms
from .models import JobOffer, JobCategory, JOB_TYPE, CURRENCY_TYPE, JobLanguage

from django import forms
from .models import JobOffer, JobCategory, JOB_TYPE, CURRENCY_TYPE, JobLanguage

class JobOfferForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=JobCategory.objects.all())
    language = forms.ModelMultipleChoiceField(queryset=JobLanguage.objects.all())

    class Meta:
        model = JobOffer
        fields = ('title', 'description', 'country', 'city', 'post_code', 'addres', 'job_type', 'category',
         'experience', 'language', 'salary', 'monthly_working_hours', 'currency')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Add Job Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Here you can add a description of the job posting', 'rows': '4'}),
            'country': forms.TextInput(attrs={'placeholder': 'e.x Poland'}),
            'city': forms.TextInput(attrs={'placeholder': 'e.x Warsaw'}),
            'post_code': forms.TextInput(attrs={'placeholder': 'e.x 03-126'}),
            'job_type': forms.Select(choices=JOB_TYPE),
            'addres': forms.TextInput(attrs={'placeholder': 'e.x Street Jana Pawła II'}),
            'experience': forms.TextInput(attrs={'placeholder': 'e.x 2 years'}),
            'salary': forms.TextInput(attrs={'placeholder': 'e.x 5000'}),
            'monthly_working_hours': forms.TextInput(attrs={'placeholder': 'e.x 160h/month'}),
            'currency': forms.Select(choices=CURRENCY_TYPE),
        }

    def __init__(self, *args, **kwargs):
        super(JobOfferForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'