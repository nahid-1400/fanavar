# Generated by Django 3.2.11 on 2023-06-03 21:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20230604_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksampel',
            name='job',
            field=models.ManyToManyField(blank=True, null=True, related_name='job_user_work_sampel', to='dashboard.Services', verbose_name='شغل'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 21, 28, 13, 402581, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
