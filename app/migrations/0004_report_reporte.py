# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181009_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reporte',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
