from tinymce.widgets import TinyMCE
from django import forms
from dashboard.models import  MyUser, Ticket
from django_summernote.widgets import SummernoteWidget
from django.core import validators
import random



class ProfileUpdateInformation(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "نام  خود را وارد کنید"}), validators=[
        validators.MaxLengthValidator(limit_value=255, message='لطفا نام  معتبر وارد کنید'),
        validators.MinLengthValidator(limit_value=2, message='لطفا نام  معتبر وارد کنید')
    ])   
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "نام خانوادگی خود را وارد کنید"}), validators=[
        validators.MaxLengthValidator(limit_value=255, message='لطفا نام خانوادگی معتبر وارد کنید'),
        validators.MinLengthValidator(limit_value=2, message='لطفا نام خانوادگی معتبر وارد کنید')
    ])   
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "شماره موبایل خود را وارد کنید"}), validators=[
        validators.MaxLengthValidator(limit_value=11, message='لطفا شماره موبایل معتبر وارد کنید'),
        validators.MinLengthValidator(limit_value=11, message='لطفا شماره موبایل معتبر وارد کنید')
    ])    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "ایمیل  خود را وارد نمایید"}),
        validators=
        [validators.EmailValidator('ایمیل وارد شده صحیح نمیباشد')])
    profile_image = forms.ImageField()


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ProfileUpdateInformation, self).__init__(*args, **kwargs)


    def clean_email(self):
        user = self.request.user
        email = self.cleaned_data.get('email')
        there_is_a_email = MyUser.objects.filter(email=email).exists()
        if user.email != email:
            if there_is_a_email:
                raise forms.ValidationError('ایمیل وجود دارد')
        return email

    def clean_phone_number(self):
        user = self.request.user
        phone_number = self.cleaned_data.get('phone_number')
        there_is_a_phone_number = MyUser.objects.filter(phone_number=phone_number).exists()
        if user.phone_number != phone_number:
            if there_is_a_phone_number:
                raise forms.ValidationError('شماره موبایل وجود دارد')
        return phone_number




class ChangePassword(forms.Form):
    password_back = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور قبلی خود را وارد نمایید'}))
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور جدید خود را وارد نمایید'}),
        validators=[
            validators.MaxLengthValidator(limit_value=50, message=' رمز عبور نمیتواند بیبشتر از 50 کاراکتر باشد'),
            validators.MinLengthValidator(limit_value=8, message='رمز عبور نمیتواند کمتر از 8 کاراکتر باشد')])
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور جدید خود را وارد نمایید'}))

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        if confirm_new_password != new_password:
            raise forms.ValidationError("رمزهای عبور مطابقت ندارند")
        return new_password
