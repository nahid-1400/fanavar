from tinymce.widgets import TinyMCE
from django import forms
from dashboard.models import  MyUser, Ticket
from django_summernote.widgets import SummernoteWidget
from django.core import validators
import random



class ProfileUpdateInformation(forms.ModelForm):
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

    class Meta:
        model = MyUser
        fields = ['first_name','last_name', 'phone_number', 'profile_image','email']


