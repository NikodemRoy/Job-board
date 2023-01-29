from django.contrib import admin

from .models import WorkerProfile, EmployerProfile

class EmployerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]


class WorkerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]
    

admin.site.register(EmployerProfile, EmployerProfileAdmin)
admin.site.register(WorkerProfile, WorkerProfileAdmin)

# Register your models here.
