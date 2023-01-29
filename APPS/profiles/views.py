from django.shortcuts import render

from APPS.accounts.decorators import user_is_employer, user_is_worker

# user_is_employer
# user_is_worker
def my_profile(request):
    return render(request, "profiles/user_profile.html")
# Create your views here.
