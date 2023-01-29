from django.contrib import admin

from .models import WorkerProfile, EmployerProfile

from APPS.job_board.models import JobOffer

class JobOfferInLine(admin.TabularInline):
    model = JobOffer
    extra = 0

class EmployerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]
    inlines = [JobOfferInLine]


class WorkerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]
    

admin.site.register(EmployerProfile, EmployerProfileAdmin)
admin.site.register(WorkerProfile, WorkerProfileAdmin)

# Register your models here.
