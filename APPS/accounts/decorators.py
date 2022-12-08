from django.core.exceptions import PermissionDenied
from functools import wraps

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