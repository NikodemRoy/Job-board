from django import views
from django.urls import path

# from django.conf import settings
# from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('employer/offer/<str:employer_id>)/create', views.create_job_offer, name="create_job_offer"),
    path('employer/offer/<int:employer_id>)/eddit/<int:offer_id>', views.eddit_job_offer, name="eddit_job_offer")

]

# serving media files
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


