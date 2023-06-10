from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from dashboard.models import Services
from django.shortcuts import redirect
from django.http import Http404, HttpResponse


class AccessUsersDashboardMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.colleague or request.user.is_author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return HttpResponse('شما اجازه دسترسی به این صفحه را ندارید.‌')
        else:
            return redirect('dashboard_user:dashboard-sigin')


