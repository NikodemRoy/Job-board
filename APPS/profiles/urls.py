from django import views
from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('worker/<str:id>', views.worker_profile, name='worker_profile'),
    path('worker/edit/<str:id>',views.eddit_worker_profile, name="eddit_worker_profile"),
    path('employer/<str:id>', views.employer_profile, name='employer_profile'),
    path('employer/edit/<str:id>', views.eddit_employer_profile, name='eddit_employer_profile'),
]

# serving media files
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


