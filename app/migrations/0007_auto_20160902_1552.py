# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160902_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='owner',
            field=models.ForeignKey(related_name='gym_owner', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
