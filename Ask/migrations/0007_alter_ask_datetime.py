# Generated by Django 3.2.9 on 2022-01-08 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Ask', '0006_alter_ask_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 1, 8, 14, 28, 50, 272773, tzinfo=utc)),
        ),
    ]
