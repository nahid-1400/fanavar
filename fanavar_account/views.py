from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from dashboard.models import MyUser, OrderDetail, Ticket, TicketAnswer
import sweetify
from django.contrib.auth import logout
from .forms import ProfileUpdateInformation,ChangePassword
from django.urls import reverse, reverse_lazy
import random
from django.contrib.auth.decorators import login_required
from .mixins import LoginMixinAccount, CheckComplateInfoUser
from utils.decorators import check_complate_info_user

@login_required(login_url='login-signup')
@check_complate_info_user
def profile_home(request):
    return render(request,'profile/profile_home.html')

class ProfileInformation(LoginMixinAccount,CheckComplateInfoUser,  DetailView):
    template_name = 'profile/profile_information_user.html'  
    model = MyUser

    def get_object(self, queryset=None):
        id = self.request.user.id
        username = self.request.user.username
        user = get_object_or_404(MyUser.objects.all(), id=id, username=username)
        return user

class ProfileOrder(LoginMixinAccount,CheckComplateInfoUser, ListView):
    template_name = 'profile/profile_orders.html'  
    model = OrderDetail

    def get_context_data(self):
        context = super().get_context_data()
        user = self.request.user
        orders = OrderDetail.objects.filter(user=user).order_by('-id')
        context['orders'] = orders
        return context


class ProfileOrderDetail(LoginMixinAccount,CheckComplateInfoUser, DetailView):
    template_name = 'profile/profile_order_detail.html'  
    model = OrderDetail

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        order = get_object_or_404(OrderDetail.objects.all(), id=id)
        return order


class ProfileTicket(LoginMixinAccount,CheckComplateInfoUser, ListView):
    template_name = 'profile/profile_tickets.html'  
    model = OrderDetail

    def get_context_data(self):
        context = super().get_context_data()
        user_id = self.request.user.id
        tickets = Ticket.objects.filter(owner=user_id).order_by('-id')
        context['tickets'] = tickets
        return context

@login_required(login_url='login-signup')
@check_complate_info_user
def profile_answer_ticket(request, id):
    user_id = request.user.id
    ticket = get_object_or_404(Ticket, owner=user_id, id=id)
    answers = TicketAnswer.objects.filter(ticket=ticket)
    if ticket.status == 'o':
        if request.method == 'POST':
            try:
                text = request.POST.get('send-answer')
                if text != '':
                    TicketAnswer.objects.create(ticket=ticket, owner=request.user, answer=text)
                else:
                    sweetify.info(request, 'لطفا پیغام خود را وارد نمایید', button='باشه', timer=3000)
            except:
                sweetify.info(request, 'لطفا پیغام خود را به درستی وارد نمایید', button='باشه', timer=3000)
    context = {'ticket':ticket, 'answers':answers}
    return render(request,'profile/profile_ticket_chat.html', context)

@login_required(login_url='login-signup')
def profile_logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login-signup')

@login_required(login_url='login-signup')
def profile_edit_information(request):
    user = request.user
    form = ProfileUpdateInformation(request.POST or None,  request=request, initial={'first_name': user.first_name, 'last_name': user.last_name, 'phone_number': user.phone_number, 'email': user.email, 'profile_image': user.profile_image})
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        phone_number = form.cleaned_data.get('phone_number')
        email = form.cleaned_data.get('email')
        profile_image = form.cleaned_data.get('profile_image')
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.email = email
        user.profile_image = profile_image
        user.save()
        sweetify.success(request, 'عملیات موفق', text='اطلاعات شما با موفقیت ویرایش و ثبت گردید', persistent='بسیار خوب')
        return redirect('profile:profile-user-informattion')
    return render(request, 'profile/profile_edit_inaformation.html', {'form':form})

@login_required(login_url='login-signup')
@check_complate_info_user
def add_new_ticket(request):
    if request.method == "POST":
        owner = request.user
        title = request.POST.get('title')
        descriptions = request.POST.get('descriptions')
        subject = request.POST.get('subject')
        print(subject)
        status = 'o'
        ticket = Ticket.objects.create(owner=owner, title=title, descriptions=descriptions, subject=subject, status=status)
        sweetify.success(request, 'تیکت شما با موفقیت ایجاد شد و به زودی به آن پاسخ خواهیم داد', button='باشه', timer=3000)
        return redirect('profile:profile-user-tickets')
    return render(request,'profile/profile_add_ticket.html')


@login_required(login_url='/login')
@check_complate_info_user
def change_password(request):
    user_id = request.user.id
    user = get_object_or_404(MyUser, id=user_id)
    change_password_form = ChangePassword(request.POST or None, initial={'password_back': user.password})
    if change_password_form.is_valid():
        password_back = change_password_form.cleaned_data.get('password_back')
        new_password = change_password_form.cleaned_data.get('new_password')
        if user.check_password(password_back):
            user.set_password(new_password)
            user.save()
            return redirect('profile:profile-user-informattion')
            sweetify.success(request, 'عملیات موفق', text='رمز عبور شما به موفقیت تغییر کرد', persistent='بسیار خوب')
        else:
            change_password_form.add_error('password_back', 'رمز عبور صحیح نیست')
    context = {'change_password': change_password_form, 'title': 'ویرایش رمز عبور'}
    return render(request, 'profile/new_password.html', context)
