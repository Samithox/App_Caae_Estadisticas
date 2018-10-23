# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181010_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='tipo_reporte',
            field=models.CharField(blank=True, max_length=30, choices=[(b'Autoreporte', b'Autoreporte'), (b'SIGAE', b'Sigae'), (b'KOLB', b'Kolb'), (b'EDWARD', b'Edward'), (b'TALL_HAB', b'Taller de Habilidades'), (b'PROPE', b'Propedeutico'), (b'HON_ALON', b'Honey Alonso'), (b'TUTORES', b'Tutores'), (b'AYUDANTIAS', b'Ayudantias')]),
        ),
    ]
