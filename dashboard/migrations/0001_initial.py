# Generated by Django 3.2.11 on 2023-05-26 18:34

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='account/user-profile', verbose_name='تصویر پروفایل')),
                ('phone_number', models.CharField(blank=True, default='0', max_length=12, null=True, verbose_name='شماره موبایل\u200c')),
                ('colleague', models.BooleanField(default=False, verbose_name='هم کار')),
                ('is_author', models.BooleanField(default=False, verbose_name='وضعیت نویسندگی')),
                ('is_coutomer', models.BooleanField(default=False, verbose_name='وضعیت مشتری')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False, verbose_name='پرداخت شده/ نشده')),
                ('payment_data', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبد های خرید',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('answer', models.TextField(verbose_name='پاسخ')),
            ],
            options={
                'verbose_name': 'سوال متداول',
                'verbose_name_plural': 'سوالات متداول',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=200, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='image_services', verbose_name='تصویر')),
                ('short_descriptions', models.TextField(blank=True, max_length=500, null=True, verbose_name='توضیحات کوتاه')),
                ('descriptions', models.TextField(verbose_name='توضیحات')),
                ('active', models.BooleanField(default=True, verbose_name='فعال')),
            ],
            options={
                'verbose_name': 'خدمت',
                'verbose_name_plural': 'خدمات',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='slider', max_length=200, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='slider', verbose_name='تصویر')),
                ('active', models.BooleanField(default=False, verbose_name='اسلایدر فعال')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('order_code', models.CharField(default=None, max_length=7, verbose_name='کد سفارش')),
                ('price', models.IntegerField(default=None, verbose_name='هزینه')),
                ('status', models.CharField(choices=[('s', 'ثبت شده'), ('a', 'در حال شروع آماده سازی'), ('p', 'شروع پروژّ'), ('k', ' در حال کار روی پروژّ '), ('e', 'اتمام پروژّ')], max_length=1, verbose_name='وضعیت')),
                ('possible_delivery_time', models.CharField(default=None, max_length=200, verbose_name='زمان احتمالی تحویل')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dashboard.order', verbose_name='سبد خرید')),
                ('servise', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='dashboard.services', verbose_name='خدمت')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارش های کاربران',
            },
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('full_name', models.CharField(max_length=120, verbose_name='نام و نام خانوادگی')),
                ('status', models.CharField(choices=[('s', 'ثبت شده'), ('e', 'در انتظار تماس'), ('m', 'معلق ')], max_length=1, verbose_name='وضعیت')),
                ('phone_number', models.IntegerField(max_length=11, verbose_name='شماره موبایل')),
                ('descriptions', models.TextField(verbose_name='توضیحات')),
                ('servise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servise_request', to='dashboard.services', verbose_name='خدمت')),
            ],
            options={
                'verbose_name': 'درخواست',
                'verbose_name_plural': 'درخواست های کاربران',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
        migrations.CreateModel(
            name='CateGoryArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='عنوان دسته بندی در url')),
                ('status', models.BooleanField(default=True, verbose_name='این دسته بندی  نمایش داده شوند؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
                ('image', models.ImageField(default='category/defualt.jpg', upload_to='category', verbose_name='تصویر دسته بندی')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='dashboard.categoryarticle', verbose_name='والد')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('short_descriptions', models.TextField(blank=True, max_length=500, null=True, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='image_post', verbose_name='تصویر')),
                ('published_time', models.DateTimeField(default=datetime.datetime(2023, 5, 26, 18, 34, 1, 674930, tzinfo=utc), verbose_name='زمان انتشار')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='اخرین به روز رسانی')),
                ('status', models.CharField(choices=[('d', ' پیش نویس'), ('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], max_length=1, verbose_name='وضعیت')),
                ('number_post', models.IntegerField(blank=True, null=True, unique=True, verbose_name='شماره پست')),
                ('active', models.BooleanField(default=True, verbose_name='فعال')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ManyToManyField(related_name='post_category', to='dashboard.CateGoryArticle', verbose_name='دسته بندی')),
                ('like_user', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='پسندها')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
                'ordering': ['-published_time'],
            },
        ),
        migrations.AddField(
            model_name='myuser',
            name='job',
            field=models.ManyToManyField(blank=True, null=True, related_name='job_user', to='dashboard.Services', verbose_name='شغل'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
