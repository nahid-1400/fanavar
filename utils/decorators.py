from django.http import HttpResponse
from django.shortcuts import redirect
import sweetify

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

def check_complate_info_user(func):
    def wapper(request, *args, **kwargs):
        email =  request.user.email
        print(email)
        if request.user.email != '':
            return func(request, *args, **kwargs)
        else:
            sweetify.info(request, 'لطفا اطلاعات خود را تکمیل کنید', button='باشه', timer=3000)
            return redirect('profile:profile-edit-information')
    return wapper