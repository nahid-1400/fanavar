from django.http import HttpResponse
from django.shortcuts import redirect


def access_user_dashboard(func):
    def wapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.colleague or request.user.is_author:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse('شما اجازه دسترسی به این صفحه را ندارید.‌')
        else:
            return redirect('dashboard_user:dashboard-sigin')
    return wapper