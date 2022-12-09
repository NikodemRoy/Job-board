from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

ACCOUNT_TYPE = [
    ('worker', 'Worker'),
    ('employer', "Employer")
]

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, error_messages={'unique': "A user with that email already exists!"})

    account_type = models.CharField(choices=ACCOUNT_TYPE,  max_length=10)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    @property
    def is_worker(self):
        return str(self.account_type) == 'worker'

    @property
    def is_manager(self):
        return str(self.account_type) == 'employer'

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, db_index=True)
    brand_name = models.CharField(max_length=96, blank=True)

class WorkerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=96, blank=True)
    surname = models.CharField(max_length=96, blank=True)