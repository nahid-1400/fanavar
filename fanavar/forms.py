from django import forms
from django.core import validators
from dashboard.models import MyUser
from django_summernote.widgets import SummernoteWidget
from dashboard.models import Demand
from dashboard.models import Services




class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "نام کاربری خود را وارد کنید"}), validators=[
        validators.MaxLengthValidator(limit_value=255, message='لطفا نام کاربری معتبر وارد کنید'),
        validators.MinLengthValidator(limit_value=2, message='لطفا نام کاربری معتبر وارد کنید')
    ])    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "شماره موبایل خود را وارد کنید"}), validators=[
        validators.MaxLengthValidator(limit_value=11, message='لطفا شماره موبایل معتبر وارد کنید'),
        validators.MinLengthValidator(limit_value=11, message='لطفا شماره موبایل معتبر وارد کنید')
    ])    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور خود را وارد نمایید'}),
        validators=[
            validators.MaxLengthValidator(limit_value=50, message=' رمز عبور نمیتواند بیبشتر از 50 کاراکتر باشد'),
            validators.MinLengthValidator(limit_value=8, message='رمز عبور نمیتواند کمتر از 8 کاراکتر باشد')])
            

    def clean_username(self):
        username = self.cleaned_data.get('username')
        there_is_a_username = MyUser.objects.filter(username=username).exists()
        if there_is_a_username:
            raise forms.ValidationError('کاربر وجود دارد')
        return username

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        there_is_a_phone_number = MyUser.objects.filter(phone_number=phone_number).exists()
        if there_is_a_phone_number:
            raise forms.ValidationError('شماره موبایل وجود دارد')
        return phone_number








class DemandForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'background-color': 'white', 'placeholder': 'لطفا عنوان خود را وارد نمایید'}), validators=[
        validators.MinLengthValidator(limit_value=2, message='لطفا عنوان معتبر وارد کنید'),
        validators.MaxLengthValidator(limit_value=50, message='لطفا عنوان معتبر وارد کنید')
    ])    
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'لطفا نام کامل خود را وارد نمایید'}), validators=[
        validators.MinLengthValidator(limit_value=11, message='لطفا نام معتبر وارد کنید'),
        validators.MaxLengthValidator(limit_value=11, message='لطفا نام معتبر وارد کنید')
    ])    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'لطفا شماره موبایل خود را وارد نمایید'}), validators=[
        validators.MaxLengthValidator(limit_value=11, message='لطفا شماره موبایل معتبر وارد کنید'),
        validators.MinLengthValidator(limit_value=11, message='لطفا شماره موبایل معتبر وارد کنید')
    ])    
    descriptions = forms.CharField(widget=forms.Textarea(attrs={'cols': '30' , 'rows':'2', 'id':'Description', 'placeholder': 'لطفا توضیحات خود را وارد نمایید'}), validators=[
        validators.MinLengthValidator(limit_value=10, message='لطفا توضیحات معتبر وارد کنید'),
        validators.MaxLengthValidator(limit_value=500, message='لطفا توضیحات معتبر وارد کنید')
    ], label='توضیحات')
