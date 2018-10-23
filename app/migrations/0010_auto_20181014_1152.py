# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20181011_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='permiso',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3')]),
        ),
    ]
