from django import views
from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('employer-registration/', views.employer_registration, name='employer_registration'),
    path('worker-registration/', views.worker_registration, name='employer_registration'),
]



