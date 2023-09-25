from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobOfferForm
from APPS.profiles.models import EmployerProfile

from APPS.accounts.decorators import user_is_employer, user_is_worker
# Create your views here.

def index_page(request):
    return render(request, "job_board/main_index.html")

@user_is_employer
def create_job_offer(request, employer_id):
    user = request.user
    profile = get_object_or_404(EmployerProfile, user=user)

    if request.method == 'POST':
        print("przechodzi POST")
        job_form= JobOfferForm(request.POST)
        print("przechodzi")
        if job_form.is_valid():
            job_offer = job_form.save(commit=False)
            job_offer.employer = get_object_or_404(EmployerProfile, id=employer_id)
            job_offer.save()
            print("powino zapisac")
            return redirect('employer_profile', id)
    else:
        print("nie dziala")
        job_form = JobOfferForm(instance=profile)

    context = {
        'job_form':job_form,
        'user':user,
    }
    return render(request, "job_board/create_job.html", context)


@user_is_employer
def eddit_job_offer(request, employer_id, offer_id):
    return redirect(index_page)