# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20181014_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reporte_Departamento',
            field=models.CharField(blank=True, max_length=50, choices=[(b'FECS', b'Facultad de Educacion y Ciencias Sociales'), (b'FACS', b'Facultad de Ciencias de la Salud '), (b'FAIN', b'Facultad de Ingenieria y Negocios'), (b'FTEO', b'Facultad de Teologia'), (b'UNACH', b'Universidad Adventista de Chile'), (b'AGRO', b'Agronomia'), (b'CON_AUD', b'Contador Auditor'), (b'ED_PARV', b'Educacion Parvularia'), (b'ENF', b'Enfermeria'), (b'ING_CIV_INF', b'Ing. Civil en Informatica'), (b'ING_INF', b'Ing. Informatica'), (b'ING_COM', b'Ing. Comercial'), (b'ING_ELEC', b'Ing. en Electronica y Telecomunicaciones'), (b'ING_CIV_IND', b'Ingenieria Civil Industrial'), (b'NUT', b'Nutricion y Dietetica'), (b'OBS', b'Obstetricia y Puericultura'), (b'PED_BIO', b'Ped. en Biologia'), (b'PED_ED_DIF', b'Ped. en Educ. Diferencial m/DEA'), (b'PED_ED_FIS', b'Ped. en Educacion Fisica'), (b'PED_ED_GEN_BAS', b'Ped. en Educacion General Basica'), (b'PED_HIS', b'Ped. en Historia y Geografia'), (b'PED_ING', b'Ped. en Ingles'), (b'PED_LENG', b'Ped. en Lengua Castellana y Comunicacion'), (b'PED_MAT', b'Ped. en Matematica y Computacion'), (b'PED_MUS', b'Ped. en Musica m/ Educacion Extraescolar'), (b'PSICO', b'Psicologia'), (b'TEO', b'Teologia'), (b'TNS_ENF', b'TNS en Enfermeria'), (b'TRAB_SOC', b'Trabajo Social')]),
        ),
    ]
