from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from dashboard.models import MyUser, OrderDetail, Ticket, TicketAnswer
import sweetify
from django.contrib.auth import logout
from .forms import ProfileUpdateInformation
from django.urls import reverse, reverse_lazy

def profile_home(request):
    return render(request,'profile/profile_home.html')

class ProfileInformation(DetailView):
    template_name = 'profile/profile_information_user.html'  
    model = MyUser

    def get_object(self, queryset=None):
        id = self.request.user.id
        username = self.request.user.username
        user = get_object_or_404(MyUser.objects.all(), id=id, username=username)
        return user

class ProfileOrder(ListView):
    template_name = 'profile/profile_orders.html'  
    model = OrderDetail

    def get_context_data(self):
        context = super().get_context_data()
        user = self.request.user
        orders = OrderDetail.objects.filter(user=user).order_by('-id')
        context['orders'] = orders
        return context


class ProfileOrderDetail(DetailView):
    template_name = 'profile/profile_order_detail.html'  
    model = OrderDetail

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        order = get_object_or_404(OrderDetail.objects.all(), id=id)
        return order


class ProfileTicket(ListView):
    template_name = 'profile/profile_tickets.html'  
    model = OrderDetail

    def get_context_data(self):
        context = super().get_context_data()
        user_id = self.request.user.id
        tickets = Ticket.objects.filter(owner=user_id).order_by('-id')
        context['tickets'] = tickets
        return context

def profile_answer_ticket(request, id):
    user_id = request.user.id
    ticket = get_object_or_404(Ticket, owner=user_id, id=id)
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
    context = {'ticket':ticket, 'answers':answers}
    return render(request,'profile/profile_ticket_chat.html', context)

def profile_logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login-signup')


class ProfileUpdateInformation(UpdateView):
    model = MyUser
    form_class = ProfileUpdateInformation
    template_name = 'profile/profile_edit_inaformation.html'
    success_url  = reverse_lazy('profile:profile-user-informattion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_obj = self.get_object()
        context['form'] = self.form_class(instance=user_obj)
        return context