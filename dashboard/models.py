from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone


class Services(models.Model):
    title = models.CharField(max_length=200, default=None, verbose_name='عنوان')
    image = models.ImageField(upload_to='image_services', verbose_name='تصویر')
    short_descriptions = models.TextField(verbose_name='توضیحات کوتاه', blank=True, null=True,  max_length=500)
    descriptions = models.TextField(verbose_name='توضیحات')
    active = models.BooleanField(default=True, verbose_name='فعال')
    show_in_work_sampel_page = models.BooleanField(default=True, verbose_name='نمایش در صفحه نمونه کارها')


    
    

    def get_absolute_url(self):
        return reverse('dashboard_user:servisees-dashboard')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'


class MyUser(AbstractUser):
    profile_image = models.ImageField(upload_to='account/user-profile', blank=True, null=True, verbose_name='تصویر پروفایل')
    phone_number = models.CharField(max_length=12, blank=True, null=True, default='0', unique=True, verbose_name='شماره موبایل‌')
    colleague = models.BooleanField(default=False, verbose_name='هم کار')
    job = models.ManyToManyField(Services, related_name='job_user', blank=True, null=True, verbose_name='شغل')
    is_author = models.BooleanField(default=False, verbose_name='وضعیت نویسندگی')
    is_coutomer = models.BooleanField(default=False, verbose_name='وضعیت مشتری')

    def get_absolute_url(self):
        return reverse('dashboard_user:user-list')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class CateGoryArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.CASCADE, related_name='children', verbose_name='والد')
    status = models.BooleanField(default=True, verbose_name='این دسته بندی  نمایش داده شوند؟')
    position = models.IntegerField(verbose_name='پوزیشن')


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(MyUser, default=None, on_delete=models.CASCADE, related_name='articles', verbose_name='نویسنده')
    STATUS_CHOICES = (
        ('d', ' پیش نویس'),
        ('p', 'منتشر شده'),
        ('i', 'در حال بررسی'),
        ('b', 'برگشت داده شده'),
    )
    title = models.CharField(max_length=200, verbose_name='عنوان')
    short_descriptions = models.TextField(verbose_name='توضیحات کوتاه', blank=True, null=True,  max_length=500)
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='image_post', verbose_name='تصویر')
    published_time = models.DateTimeField(default=timezone.now(), verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    updated = models.DateTimeField(auto_now=True, verbose_name='اخرین به روز رسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    category = models.ManyToManyField(CateGoryArticle, verbose_name='دسته بندی', related_name='post_category')
    number_post = models.IntegerField(unique=True, blank=True, null=True, verbose_name='شماره پست')
    like_user = models.ManyToManyField(MyUser, blank=True, null=True, verbose_name='پسندها')
    active = models.BooleanField(default=True, verbose_name='فعال')

    def get_absolute_url(self):
        return reverse('dashboard_user:article-list')


    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-published_time']


    def __str__(self):
        return self.title





    
class OrderDetail(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    order_code = models.CharField(max_length=7, default= None, verbose_name='کد سفارش')
    STATUS_CHOICES = (
        ('s', 'ثبت شده'),
        ('a', 'در حال شروع آماده سازی'),
        ('p', 'شروع پروژّ'),
        ('k', ' در حال کار روی پروژّ '),
        ('e', 'اتمام پروژّ'),
    )
    user = models.ForeignKey(MyUser, default=None, on_delete=models.CASCADE, verbose_name='کاربر ')
    servise = models.ForeignKey(Services, default=None, related_name='product_order', on_delete=models.CASCADE, verbose_name='خدمت')
    price = models.IntegerField(default=None, verbose_name='هزینه')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    possible_delivery_time = models.CharField(max_length=200, default= None, verbose_name='زمان احتمالی تحویل')
    description = models.TextField(verbose_name='توضیحات')

    def get_absolute_url(self):
        return reverse('dashboard_user:order-list')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش های کاربران'


    def __str__(self):
        return self.order.owner.username


class Demand(models.Model):
    STATUS_CHOICES = (
        ('s', 'ثبت شده'),
        ('e', 'در انتظار تماس'),
        ('m', 'معلق '),
    )
    title = models.CharField(max_length=120, verbose_name='عنوان')
    full_name = models.CharField(max_length=120, verbose_name='نام و نام خانوادگی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='در انتظار تماس', verbose_name='وضعیت')
    phone_number = models.IntegerField(max_length=11, verbose_name='شماره موبایل')
    descriptions = models.TextField(verbose_name='توضیحات')

    def get_absolute_url(self):
        return reverse('dashboard_user:demand-list')

    class Meta:
        verbose_name = 'درخواست'
        verbose_name_plural = 'درخواست های کاربران'


    def __str__(self):
        return self.title




TICKET_CHOICES = (
    ('t', 'درخواست اعمال تغیرات'),
    ('m', 'درخواست مشاوره'),
    ('s', 'درخواست سفارش'),
    ('g', 'گزارش مشکل'),
    ('d', 'سایر '),

)
STATUS_CHOICES = (
    ('o', 'باز'),
    ('c', 'بسته '),
)

class Ticket(models.Model):
    owner = models.ForeignKey(MyUser, default=None, on_delete=models.CASCADE, verbose_name='کاربر ')
    ticket_code = models.CharField(max_length=7, default= None, verbose_name='کد تیکت')
    title = models.CharField(max_length=200, default=None, verbose_name='عنوان')
    descriptions = models.TextField(verbose_name='توضیحات')
    subject = models.CharField(max_length=3, choices=TICKET_CHOICES, verbose_name='موضوع تیکت')
    status = models.CharField(max_length=1,default='o', choices=STATUS_CHOICES, verbose_name='وضعیت')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return self.title

class TicketAnswer(models.Model):
    ticket = models.ForeignKey(Ticket, default=None, on_delete=models.CASCADE, verbose_name='تیکت ')
    owner = models.ForeignKey(MyUser, default=None, on_delete=models.CASCADE, verbose_name='کاربر ')
    answer = models.TextField(verbose_name='پاسخ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')


    class Meta:
        verbose_name = 'پاسخ تیکت'
        verbose_name_plural = ' پاسخ تیکت ها'

    def __str__(self):
        return self.ticket.title

class Question(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    answer = models.TextField(verbose_name='پاسخ')

    class Meta:
        verbose_name = 'سوال متداول'
        verbose_name_plural = 'سوالات متداول'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('dashboard_user:question-list')






class WorkSampel(models.Model):
    title = models.CharField(max_length=120, default=None, verbose_name='عنوان')
    colleague = models.ForeignKey(MyUser, default=None, on_delete=models.CASCADE, related_name='colleague_workampel', verbose_name='هم کار')
    descriptions = models.TextField(verbose_name='توضیحات')
    link = models.CharField(max_length=120, blank=True, null=True, verbose_name='لینک')
    services = models.ForeignKey(Services, default=None, on_delete=models.CASCADE, verbose_name='خدمت')
    image = models.ImageField(upload_to='work_sampel', blank=True, null=True, default=None, verbose_name='تصویر')

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها '

    def __str__(self):
        return self.title



