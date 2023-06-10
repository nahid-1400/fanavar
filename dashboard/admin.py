from django.contrib import admin
from dashboard.models import MyUser, Services, CateGoryArticle, Article, OrderDetail, Demand,Question, WorkSampel, Ticket,TicketAnswer

admin.site.register(MyUser)
admin.site.register(Services)
admin.site.register(CateGoryArticle)
admin.site.register(Article)
admin.site.register(OrderDetail)
admin.site.register(Demand)
admin.site.register(Question)
admin.site.register(Ticket)
admin.site.register(TicketAnswer)