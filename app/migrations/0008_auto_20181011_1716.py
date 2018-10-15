# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181011_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
