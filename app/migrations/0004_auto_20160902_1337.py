# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160902_1320'),
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
    ]
