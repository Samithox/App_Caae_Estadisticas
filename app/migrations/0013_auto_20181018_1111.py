# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20181016_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tipo_Usuario',
            field=models.CharField(blank=True, max_length=25, choices=[(b'ADMINISTRATIVO', b'Administrativo'), (b'DECANO', b'Decano'), (b'DIR_CARRERA', b'Director de Carrera'), (b'SEC_ACAD', b'Secretario Academico')]),
        ),
    ]
