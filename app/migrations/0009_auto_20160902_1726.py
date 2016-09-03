# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160902_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gym',
            name='images',
        ),
        migrations.AddField(
            model_name='gym',
            name='file1',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='file2',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='file3',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='file4',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='file5',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='owner',
            field=models.ForeignKey(related_name='gym_owner', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.ImageField(null=True, upload_to=b'gym_images/', blank=True),
        ),
    ]
