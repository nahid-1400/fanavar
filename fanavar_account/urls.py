from django.urls import path
from fanavar_account.views import profile_home, ProfileInformation, ProfileOrder,  ProfileOrderDetail, ProfileTicket, profile_answer_ticket, profile_logout_user, ProfileUpdateInformation, add_new_ticket
app_name = 'profile'

urlpatterns = [
    path('home', profile_home, name='profile-home'),
    path('information', ProfileInformation.as_view(), name='profile-user-informattion'),
    path('orders', ProfileOrder.as_view(), name='profile-user-orders'),
    path('order/<id>', ProfileOrderDetail.as_view(), name='profile-user-order-detail'),
    path('tickets', ProfileTicket.as_view(), name='profile-user-tickets'),
    path('tickets/chat-ticket/<id>', profile_answer_ticket, name='profile-chat-ticket'),
    path('logout', profile_logout_user, name='profile-logout-user'),
    path('edit_information/<int:pk>', ProfileUpdateInformation.as_view(), name='profile-edit-information'),
    path('new_ticket', add_new_ticket, name='new-ticket'),



]