# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_report_reporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
