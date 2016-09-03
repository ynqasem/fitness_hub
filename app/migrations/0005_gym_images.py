# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160902_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='images',
            field=models.ManyToManyField(to='app.Image', null=True, blank=True),
        ),
    ]
