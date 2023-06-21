from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from dashboard.models import MyUser, Services,  Article, Demand, OrderDetail, Question, CateGoryArticle, Ticket,TicketAnswer, WorkSampel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from dashboard.forms import ServicesForm, ArticleForm, OrderForm, DemandForm, QuestionForm, CategoryArticelForm, UserUpdateDashboardForm, UserCreateDashboardForm, WorkSampelDashboardForm
import sweetify
from dashboard.mixins import AccessUsersDashboardMixin
from utils.decorators import access_user_dashboard
from django.db.models import Sum

def login_dashboard(request):
    error = False
    text_error = ''
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                if user.colleague is True or user.is_superuser or user.is_author:
                    login(request, user)
                    return redirect('dashboard_user:home')
                else:
                    error = True
                    text_error = 'شما اجازه دسترسی به داشبورد را ندارید'
            else:
                error = True
                text_error = 'نام کاربری  یا رمز عبور به درستی وارد نشده است'
        except ValueError:
            error = True
            text_error = 'لطفا موارد خواسته شده را به درستی وارد کنید'
    return render(request,'dashboard/signin.html', {'error': error, 'text_error': text_error})




class Dashboard(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = MyUser
    template_name = 'dashboard/home_dahsboard.html'

    def get_object(self, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id).order_by('-id')
        return user

    def get_context_data(self):
        context = super().get_context_data()
        context['users'] = MyUser.objects.filter(is_active=True).order_by('-id')
        context['services'] = Services.objects.filter(active=True)
        context['orders'] = OrderDetail.objects.all()
        context['articls'] = Article.objects.all()
        income = 0
        order_price =  OrderDetail.objects.aggregate(Sum('price'))
        for key, value in order_price.items():
            income = value
        context['ticket'] = Ticket.objects.all()
        context['income'] = income
        return context

class ServicesDashboard(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = Services
    template_name = 'dashboard/dashboard_services.html'


    def get_context_data(self):
        context = super().get_context_data()
        context['services'] = Services.objects.filter(active=True) 
        context['orders'] = OrderDetail.objects.all()       
        return context

class ServicesDetail(AccessUsersDashboardMixin, LoginRequiredMixin, DetailView):
    template_name = 'dashboard/servisees_detail.html'  

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        post = get_object_or_404(Services.objects.all(), id=id, active=True)
        return post

@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def delete_service(request, id):
    service = get_object_or_404(Services, id=id)
    if request.method == 'POST':
        service.delete()
        messages.success(request, f'خدمت مورد نظر با موفقیت حذف شد.')
        return redirect('dashboard_user:servisees-dashboard')
    context = {'object_name': service.title,'link': 'dashboard_user:servisees-dashboard'}
    return render(request, 'dashboard/confirm_delete.html', context)


class ServicesCreate(AccessUsersDashboardMixin, LoginRequiredMixin, CreateView):
    model = Services
    form_class = ServicesForm
    template_name = 'dashboard/servisees_create_update.html'

class ServicesUpdate(AccessUsersDashboardMixin, LoginRequiredMixin, UpdateView):
    model = Services
    form_class = ServicesForm
    template_name = 'dashboard/servisees_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services_obj = self.get_object()
        context['form'] = self.form_class(instance=services_obj)
        return context
    

class ArticleDashboard(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = Article
    template_name = 'dashboard/dashboard_article.html'

class ArticleCreate(AccessUsersDashboardMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'dashboard/article_create_update.html'

@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def delete_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        messages.success(request, f'مقاله مورد نظر با موفقیت حذف شد.')
        return redirect('dashboard_user:article-list')
    context = {'object_name': article.title,'link': 'dashboard_user:article-list'}
    return render(request, 'dashboard/confirm_delete.html', context)

class ArticleUpdate(AccessUsersDashboardMixin, LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'dashboard/article_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_obj = self.get_object()
        context['form'] = self.form_class(instance=article_obj)
        return context


class OrderList(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = OrderDetail
    template_name = 'dashboard/dashboard_order_list.html'

@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def delete_order(request, pk):
   
    order.delete()
    messages.success(request, f'سفارش مورد نظر با موفقیت حذف شد.')
    return redirect('dashboard_user:order-list')


@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def delete_order(request, id):
    order = get_object_or_404(OrderDetail, id=id)
    if request.method == 'POST':
        order.delete()
        messages.success(request, f'سفارش مورد نظر با موفقیت حذف شد.')
        return redirect('dashboard_user:order-list')
    context = {'object_name': order.title,'link': 'dashboard_user:order-list'}
    return render(request, 'dashboard/confirm_delete.html', context)



class OrderUpdate(AccessUsersDashboardMixin, LoginRequiredMixin ,UpdateView):
    model = OrderDetail
    form_class = OrderForm
    template_name = 'dashboard/order_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_obj = self.get_object()
        context['form'] = self.form_class(instance=order_obj)
        return context
    
class orderCreate(AccessUsersDashboardMixin, LoginRequiredMixin, CreateView):
    model = OrderDetail
    form_class = OrderForm
    template_name = 'dashboard/order_create_update.html'

class DemandList(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = Demand
    template_name = 'dashboard/dashboard_demand_list.html'


class DemandUpdate(AccessUsersDashboardMixin, LoginRequiredMixin, UpdateView):
    model = Demand
    form_class = DemandForm
    template_name = 'dashboard/demand_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        demand_obj = self.get_object()
        context['form'] = self.form_class(instance=demand_obj)
        return context

@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def demand_delete(request, id):
    demand = get_object_or_404(Demand, id=id)
    if request.method == 'POST':
        demand.delete()
        messages.success(request, f'درخواست مورد نظر با موفقیت حذف شد.')
        return redirect('dashboard_user:demand-list')
    context = {'object_name': demand.title,'link': 'dashboard_user:demand-list'}
    return render(request, 'dashboard/confirm_delete.html', context)


@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('dashboard_user:dashboard-sigin')

def sidbar_dashboard(request):
    return render(request,'dashboard/shared/sidbar.html')

class UserList(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = MyUser
    template_name = 'dashboard/dashboard_user_list.html'


    def get_context_data(self):
        context = super().get_context_data()
        context['users'] = MyUser.objects.filter(is_active=True).order_by('-id')
        return context


class UserUpdate(AccessUsersDashboardMixin, LoginRequiredMixin, UpdateView):
    model = MyUser
    form_class = UserUpdateDashboardForm
    template_name = 'dashboard/dashboard_user_create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_obj = self.get_object()
        context['form'] = self.form_class(instance=user_obj)
        return context

class UserCreate(AccessUsersDashboardMixin, LoginRequiredMixin, CreateView):
    model = MyUser
    form_class = UserCreateDashboardForm
    template_name = 'dashboard/dashboard_user_create_update.html'

@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def user_delete(request, pk):
    user = get_object_or_404(MyUser, id=pk)
    user.delete()
    messages.success(request, 'کاربر مورد نظر با موفقیت حذف شد.')
    return redirect('dashboard_user:user-list')

@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def user_delete(request, id):
    user = get_object_or_404(MyUser, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, f'کاربر مورد نظر با موفقیت حذف شد.')
        return redirect('dashboard_user:user-list')
    context = {'object_name': user.username,'link': 'dashboard_user:user-list'}
    return render(request, 'dashboard/confirm_delete.html', context)



class QuestionList(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = Question
    template_name = 'dashboard/dashboard_question.html'

class QuestionAdd(AccessUsersDashboardMixin, LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'dashboard/dashboard_add_question.html'

class QuestionUpdate(AccessUsersDashboardMixin, LoginRequiredMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'dashboard/dashboard_add_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_obj = self.get_object()
        context['form'] = self.form_class(instance=question_obj)
        return context

@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def question_delete(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        question.delete()
        messages.success(request, f'سوال مورد نظر با موفقیت حذف شد.')
        return redirect('dashboard_user:question-list')
    context = {'object_name': question.title,'link': 'dashboard_user:question-list'}
    return render(request, 'dashboard/confirm_delete.html', context)


class CateGoryArticelList(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = CateGoryArticle
    template_name = 'dashboard/dashboard_category.html'

class CateGoryArticelAdd(AccessUsersDashboardMixin, LoginRequiredMixin, CreateView):
    model = CateGoryArticle
    form_class = CategoryArticelForm
    success_url  = reverse_lazy('dashboard_user:category-list')
    template_name = 'dashboard/dashboard_add_category.html'

class CateGoryArticelUpdate(AccessUsersDashboardMixin, LoginRequiredMixin, UpdateView):
    model = CateGoryArticle
    form_class = CategoryArticelForm
    template_name = 'dashboard/dashboard_add_category.html'
    success_url  = reverse_lazy('dashboard_user:category-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_obj = self.get_object()
        context['form'] = self.form_class(instance=category_obj)
        return context

class CateGoryArticelDelete(AccessUsersDashboardMixin, LoginRequiredMixin, DeleteView):
    model = CateGoryArticle
    success_url  = reverse_lazy('dashboard_user:category-list')


@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def category_delete(request, id):
    category = get_object_or_404(CateGoryArticle, id=id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, f'دسته بندی مورد نظر با موفقیت حذف شد.')
        return redirect('dashboard_user:category-list')
    context = {'object_name': category.title,'link': 'dashboard_user:category-list'}
    return render(request, 'dashboard/confirm_delete.html', context)


class TicketList(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'dashboard/dashboard_ticket.html'

@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def answer_ticket(request, id, user_id):
    answers = ''
    tickets = ''
    ticket = get_object_or_404(Ticket, owner=user_id, id=id)
    if ticket.status == 'o':
        tickets = Ticket.objects.filter(owner=user_id, id=id)
        answers = TicketAnswer.objects.filter(ticket=ticket)
        if request.method == 'POST':
            try:
                text = request.POST.get('send-answer')
                if text != '':
                    TicketAnswer.objects.create(ticket=ticket, owner=request.user, answer=text)
                else:
                    sweetify.info(request, 'لطفا پیغام خود را وارد نمایید', button='باشه', timer=3000)
            except:
                sweetify.info(request, 'لطفا پیغام خود را به درستی وارد نمایید', button='باشه', timer=3000)
    context = {'ticket':ticket, 'answers':answers, 'tickets':tickets}
    return render(request,'dashboard/dashboard_answer_ticket.html', context)


@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def TicketDelete(request, id, user_pk):
    ticket = get_object_or_404(Ticket, id=id,  owner=user_pk)
    if request.method == 'POST':
        ticket.delete()
        messages.success(request, f'تیکت مورد نظر با موفقیت حذف شد.')
        return redirect('dashboard_user:ticket-list')
    context = {'object_name': ticket.title,'link': 'dashboard_user:ticket-list'}
    return render(request, 'dashboard/confirm_delete.html', context)


@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def clos_the_ticket(request, pk, user_pk):
    message_text = ''
    user = MyUser.objects.get(id=user_pk)
    ticket = get_object_or_404(Ticket, id=pk, owner=user)
    if ticket.status == 'o':
        ticket.status = 'c'
        message_text = 'تیکت مورد نظر با موفقیت بسته شد'
    else:
        ticket.status = 'o'
        message_text = 'تیکت مورد نظر با موفقیت باز شد'
    ticket.save()
    messages.success(request, message_text)
    return redirect('dashboard_user:ticket-list')

class WorkSampelList(AccessUsersDashboardMixin, LoginRequiredMixin, ListView):
    model = WorkSampel
    template_name = 'dashboard/dashboard_work_sampel.html'

class WorkSampelAdd(AccessUsersDashboardMixin, LoginRequiredMixin, CreateView):
    model = WorkSampel
    form_class = WorkSampelDashboardForm
    success_url  = reverse_lazy('dashboard_user:work-sampel_list')
    template_name = 'dashboard/dashboard_work_sampel_create_update.html'

class WorkSampelUpdate(AccessUsersDashboardMixin, LoginRequiredMixin, UpdateView):
    model = WorkSampel
    form_class = WorkSampelDashboardForm
    template_name = 'dashboard/dashboard_work_sampel_create_update.html'
    success_url  = reverse_lazy('dashboard_user:work-sampel_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        work_sampel_obj = self.get_object()
        context['form'] = self.form_class(instance=work_sampel_obj)
        return context

class WorkSampelDelete(AccessUsersDashboardMixin, LoginRequiredMixin, DeleteView):
    model = WorkSampel
    success_url  = reverse_lazy('dashboard_user:work-sampel_list')
    template_name = 'dashboard/confirm_delete.html'


@login_required(login_url='dashboard_user:dashboard-sigin')
@access_user_dashboard
def change_password_dashboard(request, id):
    user = MyUser.objects.get(id=id)
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')
        if new_password ==  confirm_new_password:
            user.set_password(new_password)
            user.save()
            sweetify.success(request, 'عملیات موفق', text='رمز عبور  کاربر به موفقیت تغییر کرد', persistent='بسیار خوب')
            return redirect('dashboard_user:user-list')
        else:
            sweetify.info(request, 'عملیات ناموق', text='رمز عبور و تکرار رمز عبور با هم مغایرت ندارند', persistent='بسیار خوب')
    context = {'user': user}
    return render(request, 'dashboard/change_password.html', context)
