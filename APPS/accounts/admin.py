from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, EmployerProfile, WorkerProfile
from .forms import RegisterForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'account_type',)
    list_filter = ('email', 'is_staff', 'is_active', 'account_type',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'account_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'account_type')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class EmployerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]


class WorkerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["user",]
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(EmployerProfile, EmployerProfileAdmin)
admin.site.register(WorkerProfile, WorkerProfileAdmin)
