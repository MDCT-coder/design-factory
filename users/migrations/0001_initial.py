# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 02:57
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='\u90ae\u7bb1')),
                ('username', models.CharField(max_length=63, unique=True, verbose_name='\u7528\u6237\u540d')),
                ('short_desc', models.CharField(max_length=255, verbose_name='\u7b80\u4ecb')),
                ('is_staff', models.BooleanField(default=False, verbose_name='\u804c\u5458\u72b6\u6001')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u8d26\u6237\u72b6\u6001')),
                ('subscribed', models.BooleanField(default=True, verbose_name='\u8ba2\u9605')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='\u6ce8\u518c\u65f6\u95f4')),
                ('verification_code', models.CharField(blank=True, max_length=31, null=True, verbose_name='\u9a8c\u8bc1\u7801')),
                ('verification_code_expired_at', models.DateTimeField(blank=True, null=True, verbose_name='\u9a8c\u8bc1\u7801\u8fc7\u671f\u65f6\u95f4')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
