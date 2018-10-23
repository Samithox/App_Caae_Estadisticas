# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181011_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='tipo_reporte',
            field=models.CharField(blank=True, max_length=30, choices=[(b'Autoreporte', b'Autoreporte'), (b'Sigae', b'Sigae'), (b'Kolb', b'Kolb'), (b'Edward', b'Edward'), (b'Taller_Habilidades', b'Taller de Habilidades'), (b'Propedeutico', b'Propedeutico'), (b'Honey_Alonso', b'Honey Alonso'), (b'Tutores', b'Tutores'), (b'Ayudantias', b'Ayudantias')]),
        ),
    ]
