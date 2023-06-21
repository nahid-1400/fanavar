from django.shortcuts import redirect
import sweetify

class LoginMixinAccount():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('login-signup')


class CheckComplateInfoUser():
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.email != '':
            return super().dispatch(request, *args, **kwargs)
        else:
            sweetify.info(request, 'لطفا اطلاعات خود را تکمیل کنید', button='باشه', timer=3000)
            return redirect('profile:profile-edit-information')

