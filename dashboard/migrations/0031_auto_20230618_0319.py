# Generated by Django 3.2.11 on 2023-06-17 23:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_auto_20230608_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_code',
        ),
        migrations.AlterField(
            model_name='article',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 17, 23, 49, 29, 551187, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
