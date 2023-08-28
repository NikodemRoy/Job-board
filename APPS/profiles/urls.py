from django import views
from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('<str:id>', views.worker_profile, name='worker_profile'),
    path('edit/<str:id>',views.eddit_worker_profile, name="eddit_worker_profile"),
]

# serving media files
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


