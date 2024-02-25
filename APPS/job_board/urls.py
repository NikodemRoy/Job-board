from django import views
from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('employer/offer/create/<str:employer_id>', views.create_job_offer, name="create_job_offer"),
    path('employer/offer/manage/<str:employer_id>', views.manage_job_offer, name="manage_job_offer"),
    path('employer/offer/eddit/<str:employer_id>/<int:offer_id>', views.eddit_job_offer, name="eddit_job_offer"),


]

# serving media files
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


