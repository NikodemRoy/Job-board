from django.contrib import admin

from .models import JobOffer, JobCategory

class JobOfferAdmin(admin.ModelAdmin):
    list_display = ['employer', 'title', 'job_type', 'created_date',]
    list_filter = ['is_published',]
    search_fields = ['employer__user__email','title',]


admin.site.register(JobCategory)
admin.site.register(JobOffer, JobOfferAdmin)


# Register your models here.
