from django.core.exceptions import PermissionDenied
from functools import wraps
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def user_is_employer(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):   
        if request.user.role == 'employer':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap



def user_is_worker(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):    
        if request.user.role == 'worker':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap

def employee_required(
        function=None,
        redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.account_type == 'worker',
        redirect_field_name=redirect_field_name,
        login_url=login_url)

    if function:
        return actual_decorator(function)

    return actual_decorator


def manager_required(
        function=None,
        redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.account_type == 'employer',
        redirect_field_name=redirect_field_name,
        login_url=login_url)

    if function:
        return actual_decorator(function)

    return actual_decorator