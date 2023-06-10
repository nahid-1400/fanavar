from tinymce.widgets import TinyMCE
from django import forms
from django.utils.html import escape, mark_safe
from dashboard.models import Services, Article, OrderDetail, Demand, MyUser, Question, CateGoryArticle
from django_summernote.widgets import SummernoteWidget


class ServicesForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    descriptions = forms.CharField(widget=SummernoteWidget())

    
    class Meta:
        model = Services
        fields = ['title', 'image','short_descriptions', 'descriptions', 'active']

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Article
        fields = ['author', 'title','short_descriptions', 'image', 'description','published_time','status','category','number_post']


class OrderForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = OrderDetail
        fields = ['title', 'order_code', 'servise','user',  'price','status','possible_delivery_time','description']


class DemandForm(forms.ModelForm):
    descriptions = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Demand
        fields = ['title', 'full_name','status', 'phone_number', 'descriptions']


class UserCreateDashboardForm(forms.ModelForm):
    username = forms.CharField(label='نام کاربری')
    first_name = forms.CharField(label=' نام')
    last_name = forms.CharField(label=' نام خانوادگی')


    class Meta:
        model = MyUser
        fields = ['username', 'first_name','last_name', 'phone_number','password', 'profile_image','colleague','job','is_author','is_coutomer']
        help_texts = {
            "username":None,
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserUpdateDashboardForm(forms.ModelForm):
    username = forms.CharField(label='نام کاربری')
    first_name = forms.CharField(label=' نام')
    last_name = forms.CharField(label=' نام خانوادگی')


    class Meta:
        model = MyUser
        fields = ['username', 'first_name','last_name', 'phone_number', 'profile_image','colleague','job','is_author','is_coutomer']
        help_texts = {
            "username":None,
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'answer']


class CategoryArticelForm(forms.ModelForm):
    class Meta:
        model = CateGoryArticle
        fields = ['title', 'parent', 'status', 'position']


