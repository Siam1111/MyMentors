# Generated by Django 3.2.9 on 2022-01-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images')),
                ('about', models.TextField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
