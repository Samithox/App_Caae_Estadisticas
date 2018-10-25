# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rut_Cliente', models.CharField(max_length=9)),
                ('nombre_Cliente', models.CharField(max_length=50)),
                ('email_Cliente', models.CharField(max_length=100)),
                ('telefono_Cliente', models.IntegerField(max_length=20)),
                ('tipo_Reserva', models.CharField(blank=True, max_length=20, choices=[(b'Con Reserva', b'Con Reserva'), (b'Sin Reserva', b'Sin Reserva')])),
            ],
        ),
    ]
