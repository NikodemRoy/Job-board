from django.shortcuts import render

def my_profile(request):
    return render(request, "profiles/user_profile.html")
# Create your views here.
