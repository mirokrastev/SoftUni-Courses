from django.shortcuts import render


def allowed_groups(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles or request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            return render(request, 'unauthorized.html')
        return wrapper
    return decorator
