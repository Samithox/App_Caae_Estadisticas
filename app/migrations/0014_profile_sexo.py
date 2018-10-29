# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20181018_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sexo',
            field=models.CharField(blank=True, max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
        ),
    ]
