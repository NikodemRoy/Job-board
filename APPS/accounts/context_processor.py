from allauth.account.forms import SignupForm, LoginForm
from .forms import WorkerSignupForm, RegisterForm

def login_ctx_tag(request):
    return {'loginctx': LoginForm()}