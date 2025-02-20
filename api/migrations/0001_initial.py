# Generated by Django 5.0.6 on 2024-06-24 07:23

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=100)),
                ('employeeid', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_driver', models.BooleanField(default=False)),
                ('car_model', models.CharField(blank=True, max_length=100, null=True)),
                ('license_plate', models.CharField(blank=True, max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabNumber', models.CharField(max_length=100)),
                ('start', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('availableSeats', models.SmallIntegerField()),
                ('startTime', models.TimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(auto_now_add=True)),
                ('driver', models.ForeignKey(limit_choices_to={'is_driver': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cabNumber', models.CharField(max_length=100)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('driver', models.ForeignKey(limit_choices_to={'is_driver': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
