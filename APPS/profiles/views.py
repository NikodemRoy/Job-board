from django.shortcuts import render


from APPS.accounts.decorators import user_is_employer, user_is_worker
from .models import WorkerProfile, EmployerProfile
# user_is_employer

@user_is_worker
def my_profile(request):
    user = request.user
    profile = WorkerProfile.objects.get(user=user)

    user_email = user.email

    user_name = profile.name
    user_surname = profile.surname
    user_phone = profile.phone_number
    user_languages = profile.languages
    user_title = profile.job_title
    user_birth = profile.age


    context = {
        "user_email":user_email,
        "user_name":user_name,
        "user_surname":user_surname,
        "user_phone":user_phone,
        "user_birth":user_birth,
        }
    return render(request, "profiles/user_profile.html", context)
# Create your views here.
