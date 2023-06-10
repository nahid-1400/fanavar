from django.urls import path
from dashboard.views import login_dashboard, Dashboard, logout_user, sidbar_dashboard,ServicesDashboard, ServicesDetail, ServicesCreate, delete_service, ServicesUpdate, ArticleDashboard, ArticleCreate, delete_article, ArticleUpdate, OrderList, delete_order, OrderUpdate,orderCreate, DemandList, DemandUpdate, UserList, UserUpdate, UserCreate, demand_delete, user_delete,QuestionList, QuestionAdd, QuestionUpdate, QuestionDelete,CateGoryArticelList,CateGoryArticelAdd,CateGoryArticelUpdate,CateGoryArticelDelete, TicketList, answer_ticket, TicketDelete, clos_the_ticket


app_name = 'dashboard_user'

urlpatterns = [
    path('', Dashboard.as_view(), name='home'),
    path('sigin', login_dashboard, name='dashboard-sigin'),
    path('logout', logout_user, name='logout-user'),
    path('sidbar_dashboard', sidbar_dashboard, name='sidbar-dashboard'),
    path('servisees', ServicesDashboard.as_view(), name='servisees-dashboard'),
    path('servise/update/<int:pk>', ServicesUpdate.as_view(), name='servise-update'),
    path('article/update/<int:pk>', ArticleUpdate.as_view(), name='article-update'),
    path('order/update/<int:pk>', OrderUpdate.as_view(), name='order-update'),
    path('demand/update/<int:pk>', DemandUpdate.as_view(), name='demand-update'),
    path('user/update/<int:pk>', UserUpdate.as_view(), name='user-update'),
    path('question/update/<int:pk>', QuestionUpdate.as_view(), name='question-update'),
    path('category/update/<int:pk>', CateGoryArticelUpdate.as_view(), name='category-update'),
    path('servise/<title>/<id>', ServicesDetail.as_view(), name='servisees-detail'),
    path('article/create', ArticleCreate.as_view(), name='article-create'),
    path('order/create', orderCreate.as_view(), name='order-create'),
    path('user/create', UserCreate.as_view(), name='user-create'),
    path('article/delete/<id>', delete_article, name='article-delete'),
    path('servise/create', ServicesCreate.as_view(), name='servise-create'),
    path('question/add', QuestionAdd.as_view(), name='question-add'),
    path('category/add', CateGoryArticelAdd.as_view(), name='category-add'),
    path('services/delete/<int:id>/', delete_service, name='delete-service'),
    path('articles', ArticleDashboard.as_view(), name='article-list'),
    path('orders', OrderList.as_view(), name='order-list'),
    path('orders/delete/<int:pk>', delete_order, name='order-delete'),
    path('demand', DemandList.as_view(), name='demand-list'),
    path('demand/delete/<int:pk>', demand_delete, name='demand-delete'),
    path('question/delete/<int:pk>', QuestionDelete.as_view(), name='question-delete'),
    path('users', UserList.as_view(), name='user-list'),
    path('user/delete/<int:pk>', user_delete, name='user-delete'),
    path('ticket/delete/<int:pk>/<user_pk>', TicketDelete, name='ticket-delete'),
    path('category/delete/<int:pk>', CateGoryArticelDelete.as_view(), name='category-delete'),
    path('questions', QuestionList.as_view(), name='question-list'),
    path('cate_gory_list', CateGoryArticelList.as_view(), name='category-list'),
    path('tickets', TicketList.as_view(), name='ticket-list'),
    path('ticket/answer/<id>/<user_id>', answer_ticket, name='answer-ticket'),
    path('ticket/close_ticket/<pk>/<user_pk>', clos_the_ticket, name='close-ticket')





]