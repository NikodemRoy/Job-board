from django.db import models

from APPS.profiles.models import WorkerProfile, EmployerProfile

JOB_TYPE = (
    ("Full time", "Full time"),
    ("Part time", "Part time"),
    ("Internship", "Internship"),
    ("Freelance", "Freelance"),
    ("Temporary", "Temporary"),
)

CURRENCY_TYPE = (
    ("PLN", "PLN"),
    ("EUR", "EUR"),
    ("USD", "USD"),
)

class JobCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class JobLanguage(models.Model):
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.language

class JobOffer(models.Model):
    employer = models.ForeignKey(EmployerProfile, related_name='EmployerProfile', on_delete=models.CASCADE)

    title = models.CharField(max_length=300)
    description = models.TextField(max_length=20000)
    country = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=300)
    post_code = models.CharField(max_length=300)
    addres = models.CharField(max_length=300)

    job_type = models.CharField(choices=JOB_TYPE, max_length=30)
    category = models.ManyToManyField(JobCategory, blank=True)
    experience = models.CharField(max_length=4)
    language = models.ManyToManyField(JobLanguage, blank=True)

    salary = models.CharField(max_length=30, blank=True)
    monthly_working_hours = models.CharField(max_length=30)
    currency = models.CharField(choices=CURRENCY_TYPE, max_length=3)

    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def hourly_wage(self):
        if self.salary and self.monthly_working_hours is not None:
            wage = float(self.salary/self.monthly_working_hours )
        return wage

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_date']

# Create your models here.
