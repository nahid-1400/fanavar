# Generated by Django 3.2.11 on 2023-06-03 22:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20230604_0143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worksampel',
            old_name='service',
            new_name='services',
        ),
        migrations.AlterField(
            model_name='article',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 3, 22, 14, 17, 442152, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]