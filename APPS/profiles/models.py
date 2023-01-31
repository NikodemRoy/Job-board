from django.db import models

from datetime import date

from APPS.accounts.models import CustomUser

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, db_index=True)

    brand_name = models.CharField(max_length=96, blank=True)
    logo = models.ImageField(upload_to='company_logo', default='company_logo/defoult_logo.jpg')
    banner = models.ImageField(upload_to='company_baner', default='company_logo/defoult_baner.jpg')

    address = models.CharField(max_length=96, blank=True)
    foundation_year = models.CharField(max_length=96, blank=True)
    phone_number = models.CharField(max_length=96, blank=True)
    number_of_workers = models.CharField(max_length=15, blank=True)
    contact_email = models.CharField(max_length=96, blank=True)
    website = models.CharField(max_length=96, blank=True)

    fb_link = models.CharField(max_length=96, blank=True)
    twitter_link = models.CharField(max_length=96, blank=True)
    linkedin_link = models.CharField(max_length=96, blank=True)
    instagram_link = models.CharField(max_length=96, blank=True)
    youtube_link = models.CharField(max_length=96, blank=True)

    company_description = models.TextField(max_length=5000, blank=True)

    def __str__(self):
        return self.user.email

class WorkerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, db_index=True)

    name = models.CharField(max_length=96, blank=True)
    surname = models.CharField(max_length=96, blank=True)
    phone_number = models.CharField(max_length=96, blank=True)


    languages = models.CharField(max_length=96, blank=True)
    job_title = models.CharField(max_length=96, blank=True)
    work_experience = models.CharField(max_length=4, blank=True)
    birth_year = models.CharField(max_length=4, blank=True)

    country = models.CharField(max_length=96, blank=True)
    city = models.CharField(max_length=96, blank=True)

    profile_description = models.TextField(max_length=5000, blank=True)

    fb_link = models.CharField(max_length=96, blank=True)
    twitter_link = models.CharField(max_length=96, blank=True)
    linkedin_link = models.CharField(max_length=96, blank=True)
    instagram_link = models.CharField(max_length=96, blank=True)
    youtube_link = models.CharField(max_length=96, blank=True)

    def age(self):
        year = date.today().year
        if self.birth_year:
            birth_year = int(self.birth_year)
            age = int(year - birth_year)
            return str(age)
        else:
            pass 

    def __str__(self):
        return self.user.email

class ShortSkills(models.Model):
    profile = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, null=True, blank=True)
    skill = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.skill)

class Skills(models.Model):
    profile = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, null=True, blank=True)
    skill = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    work_experience = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return str(self.skill)

class EmploymentHistory(models.Model):
    profile = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    position_name = models.CharField(max_length=200, blank=True, null=True)
    job_description = models.CharField(max_length=200, blank=True, null=True)

    from_date = models.CharField(max_length=15, blank=True, null=True)
    to_date = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return str(self.position_name)

class EducationHistory(models.Model):
    profile = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, null=True, blank=True)
    schoole_name = models.CharField(max_length=200, blank=True, null=True)
    title_name = models.CharField(max_length=200, blank=True, null=True)
    schoole_description = models.CharField(max_length=200, blank=True, null=True)

    from_date = models.CharField(max_length=15, blank=True, null=True)
    to_date = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return str(self.schoole_name)

class CertificatesHistory(models.Model):
    profile = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, null=True, blank=True)
    certificate_name = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    job_description = models.CharField(max_length=200, blank=True, null=True)

    from_date = models.CharField(max_length=15, blank=True, null=True)
    to_date = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return str(self.certificate_name)
