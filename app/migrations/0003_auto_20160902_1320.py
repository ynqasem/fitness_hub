# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_gym_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='gym',
            name='lati',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='gym',
            name='longi',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
