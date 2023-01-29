from django.contrib import admin

from .models import WorkerProfile, EmployerProfile, ShortSkills, Skills, EducationHistory, EmploymentHistory

from APPS.job_board.models import JobOffer


class JobOfferInLine(admin.TabularInline):
    model = JobOffer
    extra = 0

class EmployerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]
    inlines = [JobOfferInLine]


class ShortSkillsInLine(admin.TabularInline):
    model = ShortSkills
    extra = 0

class SkillsInLine(admin.TabularInline):
    model = Skills
    extra = 0

class EducationHistoryInLine(admin.TabularInline):
    model = EducationHistory
    extra = 0

class EmploymentHistoryInLine(admin.TabularInline):
    model = EmploymentHistory
    extra = 0

class WorkerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]
    inlines = [ShortSkillsInLine, SkillsInLine, EducationHistoryInLine, EmploymentHistoryInLine,]
    

admin.site.register(EmployerProfile, EmployerProfileAdmin)
admin.site.register(WorkerProfile, WorkerProfileAdmin)

# Register your models here.
