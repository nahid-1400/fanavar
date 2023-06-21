from django.shortcuts import render, redirect, get_object_or_404
from dashboard.models import Services, Article, Question, MyUser, Demand, WorkSampel
from django.contrib.auth import authenticate, login, logout
import sweetify
from fanavar.forms import SignupForm, DemandForm
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse
import itertools

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def home(request):
    servises = Services.objects.filter(active=True).order_by('-id')
    articles = Article.objects.filter(status='p').order_by('-id')
    questions = Question.objects.all().order_by('-id')  
    context = {'servises':servises, 'articles':articles, 'questions':questions}
    return render(request,'fanavar/index.html', context)



def login_signup(request):
    error = False
    text_error = ''
    signup_form = SignupForm(request.POST or None)
    if request.method == 'POST':
        if 'login_btn' in request.POST:
            try:
                username = request.POST.get('username')
                password = request.POST.get('pswd')
                user = authenticate(request, username=username, password=password)
                if user is not None: 
                    login(request, user)
                    sweetify.success(request, 'شما با موفقیت وارد حساب کاربری خود شدید.', button='باشه', timer=3000)
                    return redirect('profile:profile-home')
                else:
                    sweetify.info(request, 'نام کاربری  یا رمز عبور به درستی وارد نشده است', button='باشه', timer=3000)
            except ValueError:
                sweetify.info(request,'لطفا موارد خواسته شده را به درستی وارد کنید', button='باشه', timer=3000)
    if 'siginup_btn' in request.POST:
        if signup_form.is_valid():
            user_name = signup_form.cleaned_data.get('username')
            phone_number = signup_form.cleaned_data.get('phone_number')
            password = signup_form.cleaned_data.get('password')
            try:
                user = MyUser.objects.create_user(username=user_name, phone_number=phone_number, password=password)
                sweetify.success(request, 'حساب شما با موفقیت ایجاد شد ', button='باشه', timer=3000)
                login(request, user)
                return redirect('profile:profile-home')
            except ValueError:
                sweetify.info(request,'لطفا موارد خواسته شده را به درستی وارد کنید', button='باشه', timer=3000)
    context = {'signup_form':signup_form}
    return render(request,'fanavar/login-sign-up.html', context)

def dmand_create(request):
    demand_form = DemandForm(request.POST or None)
    if demand_form.is_valid():
        title = demand_form.cleaned_data.get('title')
        full_name = demand_form.cleaned_data.get('full_name')
        phone_number = demand_form.cleaned_data.get('phone_number')
        descriptions = demand_form.cleaned_data.get('descriptions')
        try:
            dmand = Demand.objects.create(title=title, full_name=full_name, phone_number=phone_number,status='e', descriptions=descriptions)
            sweetify.success(request, 'درخواست شما با موفقیت ثبت شد', button='باشه', timer=3000)
            return redirect('home')
        except ValueError:
            sweetify.info(request,'لطفا موارد خواسته شده را به درستی وارد کنید', button='باشه', timer=3000)
    context = {'form':demand_form}
    return render(request,'fanavar/adviser-and-order.html', context)


class ServicesView(ListView):
    model = Services
    template_name = 'fanavar/services.html'

class ArticleView(ListView):
    model = Article
    paginate_by = 8
    template_name = 'fanavar/articels.html'

    def get_queryset(self):
        articel = Article.objects.filter(status='p')
        g_articel = list(my_grouper(4, articel))
        return g_articel

class WorkSampelView(ListView):
    model = WorkSampel
    template_name = 'fanavar/work_sampels.html'


    def get_context_data(self):
        context = super().get_context_data()
        context['services'] = Services.objects.filter(show_in_work_sampel_page=True)    
        context['work_sampels']  = WorkSampel.objects.all()
        return context


class ServicesDetailFanavar(DetailView):
    template_name = 'fanavar/service_page.html'  
    model = Services

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        title = self.kwargs.get('title')
        service = get_object_or_404(Services.objects.all(), id=id, active=True)
        return service

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['services'] = Services.objects.filter(active=True)      
        return context

class ArticelDetailFanavar(DetailView):
    template_name = 'fanavar/articel_page.html'  
    model = Article

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        title = self.kwargs.get('title')
        articel = get_object_or_404(Article.objects.all(), id=id, active=True)
        return articel

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['articels'] = Article.objects.filter(active=True)      
        return context

class AboutUs(TemplateView):
    template_name = 'fanavar/about_us.html' 

class ContactUs(TemplateView):
    template_name = 'fanavar/contact_us.html' 

class Guide(TemplateView):
    template_name = 'fanavar/guide.html' 
