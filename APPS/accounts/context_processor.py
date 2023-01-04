from allauth.account.forms import SignupForm
from .forms import WorkerSignupForm, RegisterForm

def login_ctx_tag(request):
    return {'loginctx': RegisterForm()}