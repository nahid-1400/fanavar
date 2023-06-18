from django.shortcuts import redirect

class LoginMixinAccount():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('login-signup')


