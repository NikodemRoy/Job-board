from django.shortcuts import render

def register(request):
    return render(request, 'accounts/login.html')
# Create your views here.
