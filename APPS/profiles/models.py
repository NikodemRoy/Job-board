from django.db import models

from APPS.accounts.models import CustomUser

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, db_index=True)
    brand_name = models.CharField(max_length=96, blank=True)

    def __str__(self):
        return self.user.email

class WorkerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=96, blank=True)
    surname = models.CharField(max_length=96, blank=True)

    def __str__(self):
        return self.user.email

# Create your models here.
