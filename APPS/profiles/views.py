from django.shortcuts import get_object_or_404, redirect, render


from APPS.accounts.decorators import user_is_employer, user_is_worker
from .models import WorkerProfile, EmployerProfile
from .forms import WorkerProfileForm
# user_is_employer

@user_is_worker
def worker_profile(request, id):
    user = request.user
    profile = WorkerProfile.objects.get(user=user)

    user_email = user.email

    user_name = profile.name
    user_surname = profile.surname
    user_phone = profile.phone_number
    user_languages = profile.languages
    user_title = profile.job_title
    user_birth = profile.age

    user_country = profile.country
    user_city = profile.city

    user_description = profile.profile_description

    fb_link = profile.fb_link
    twitter_link = profile.twitter_link
    linkedin_link = profile.linkedin_link
    instagram_link = profile.instagram_link
    youtube_link = profile.youtube_link

    context = {
        "user_email":user_email,
        "user_name":user_name,
        "user_surname":user_surname,
        "user_phone":user_phone,
        "user_birth":user_birth,
        "user_country":user_country,
        "user_city":user_city,
        "user_description":user_description,
        "fb_link":fb_link,
        "twitter_link":twitter_link,
        "linkedin_link":linkedin_link,
        "instagram_link":instagram_link,
        "youtube_link":youtube_link,
        }

    return render(request, "profiles/user_profile.html", context)

@user_is_worker
def eddit_worker_profile(request, id):
    user = request.user
    profile = get_object_or_404(WorkerProfile, user=user)

    
    if request.method == 'POST':
        profile_form = WorkerProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            print("powino zapisac")
            return redirect('worker_profile', id)
    else:
        profile_form = WorkerProfileForm(instance=profile)

    context = {
        'profile_form':profile_form,
        'user':user,
    }
    return render(request, "profiles/eddit_profile.html", context)

# @user_is_worker
# def eddit_my_profile(request, id):
#     user = request.user
#     profile = WorkerProfile.objects.get(user=user)

#     user_email = user.email

#     user_name = profile.name
#     user_surname = profile.surname
#     user_phone = profile.phone_number
#     user_languages = profile.languages
#     user_title = profile.job_title
#     user_birth = profile.age

#     user_country = profile.country
#     user_city = profile.city

#     user_description = profile.profile_description

#     fb_link = profile.fb_link
#     twitter_link = profile.twitter_link
#     linkedin_link = profile.linkedin_link
#     instagram_link = profile.instagram_link
#     youtube_link = profile.youtube_link

#     context = {
#         "user_email":user_email,
#         "user_name":user_name,
#         "user_surname":user_surname,
#         "user_phone":user_phone,
#         "user_birth":user_birth,
#         "user_country":user_country,
#         "user_city":user_city,
#         "user_description":user_description,
#         "fb_link":fb_link,
#         "twitter_link":twitter_link,
#         "linkedin_link":linkedin_link,
#         "instagram_link":instagram_link,
#         "youtube_link":youtube_link,
#         }
#     return render(request, "profiles/eddit_profile.html", context)


