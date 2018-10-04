# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='usuario',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='profile',
            name='permiso',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3')]),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
