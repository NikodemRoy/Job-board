from django import views
from django.urls import path, include

# from django.conf import settings
# from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('accounts/', include('allauth.urls')),
    path('worker/signup', views.WorkerSignupView.as_view(), name='worker_signup'),
    path('employer/signup', views.EmployerSignupView.as_view(), name='employer_signup'),
]



