# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_gym_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gym',
            name='file1',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='file2',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='file3',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='file4',
        ),
        migrations.RemoveField(
            model_name='gym',
            name='file5',
        ),
    ]
