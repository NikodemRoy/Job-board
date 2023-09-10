from django.shortcuts import render, redirect

from APPS.accounts.decorators import user_is_employer, user_is_worker
# Create your views here.

def index_page(request):
    return render(request, "job_board/main_index.html")

@user_is_employer
def create_job_offer(request, employer_id):
    return redirect(index_page)

@user_is_employer
def eddit_job_offer(request, employer_id, offer_id):
    return redirect(index_page)