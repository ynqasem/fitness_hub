# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name=b'first name', blank=True)),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name=b'last name', blank=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'active')),
                ('owner', models.BooleanField(default=False, verbose_name=b'Owner Status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name=b'date joined')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gym_name', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('location', models.CharField(max_length=255, null=True, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'Z', b'Mixed')])),
                ('number', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_name', models.CharField(max_length=100, null=True, blank=True)),
                ('file', models.ImageField(null=True, upload_to=b'gym_images/', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='gym',
            name='images',
            field=models.ManyToManyField(to='app.Image', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='members',
            field=models.ManyToManyField(related_name='gym_members', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='owner',
            field=models.ForeignKey(related_name='gym_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
