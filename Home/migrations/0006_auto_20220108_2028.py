# Generated by Django 3.2.9 on 2022-01-08 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20220108_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 1, 8, 14, 28, 45, 475166, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 1, 8, 14, 28, 45, 475166, tzinfo=utc)),
        ),
    ]
