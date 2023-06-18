# Generated by Django 3.2.11 on 2023-06-17 23:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_auto_20230618_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 17, 23, 56, 19, 489356, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='subject',
            field=models.CharField(choices=[('t', 'درخواست اعمال تغیرات'), ('m', 'درخواست مشاوره'), ('s', 'درخواست سفارش'), ('g', 'گزارش مشکل'), ('d', 'سایر ')], max_length=3, verbose_name='موضوع تیکت'),
        ),
    ]
