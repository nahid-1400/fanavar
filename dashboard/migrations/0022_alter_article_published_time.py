# Generated by Django 3.2.11 on 2023-06-05 20:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_alter_article_published_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 5, 20, 12, 35, 603542, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]