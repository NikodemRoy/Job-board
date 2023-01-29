from locale import currency
from django.db import models

from APPS.accounts.models import WorkerProfile, EmployerProfile

JOB_TYPE = (
    ("Full time", "Full time"),
    ("Part time", "Part time"),
    ("Internship", "Internship"),
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

class JobOffer(models.Model):
    employer = models.ForeignKey(EmployerProfile, related_name='EmployerProfile', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=20000)
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=30)
    category = models.ForeignKey(JobCategory,related_name='Category', on_delete=models.CASCADE, blank=True)
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

# Create your models here.
