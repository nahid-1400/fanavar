"""fanavaran_web_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from fanavar.views import home, login_signup, dmand_create, ServicesView, ArticleView,WorkSampelView, ServicesDetailFanavar, ArticelDetailFanavar, AboutUs, ContactUs, Guide

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('profile/', include('fanavar_account.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', home, name='home'),
    path('login_signup', login_signup, name='login-signup'),
    path('demand_create', dmand_create , name='demand-create'),
    path('services', ServicesView.as_view() , name='services'),
    path('articels', ArticleView.as_view() , name='articels'),
    path('articels/page/<int:page>', ArticleView.as_view() , name='articels'),
    path('work_sampels', WorkSampelView.as_view() , name='work-sampels'),
    path('service/<id>/<title>', ServicesDetailFanavar.as_view() , name='service-fanavar'),
    path('articel/<id>/<title>', ArticelDetailFanavar.as_view() , name='articel-fanavar'),
    path('about_us', AboutUs.as_view() , name='about-us'),
    path('contact_us', ContactUs.as_view() , name='contact-us'),
    path('guide', Guide.as_view() , name='guide'),






]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)