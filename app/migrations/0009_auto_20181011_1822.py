# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181011_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facultad',
            field=models.CharField(blank=True, max_length=5, choices=[(b'FECS', b'Facultad de Educacion y Ciencias Sociales'), (b'FACS', b'Facultad de Ciencias de la Salud'), (b'FAIN', b'Facultad de Ingenieria y Negocios'), (b'FTEO', b'Facultad de Teologia'), (b'UNACH', b'Universidad Adventista de Chile')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='permiso',
            field=models.CharField(blank=True, max_length=1, choices=[(1, 1), (2, 2), (3, 3)]),
        ),
    ]
