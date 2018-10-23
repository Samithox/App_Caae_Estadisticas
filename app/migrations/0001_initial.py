# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facultad', models.CharField(blank=True, max_length=5, choices=[(b'FECS', b'Facultad de Educacion y Ciencias Sociales'), (b'FACS', b'Facultad de Ciencias de la Salud'), (b'FAIN', b'Facultad de Ingenieria y Negocios'), (b'FTEO', b'Facultad de Teologia'), (b'UNACH', b'Universidad Adventista de Chile')])),
                ('carrera', models.CharField(blank=True, max_length=50, choices=[(b'ALL', b'Todas'), (b'AGRO', b'Agronomia'), (b'CON_AUD', b'Contador Auditor'), (b'ED_PARV', b'Educacion Parvularia'), (b'ENF', b'Enfermeria'), (b'ING_CIV_INF', b'Ing. Civil en Informatica'), (b'ING_COM', b'Ing. Comercial'), (b'ING_ELEC', b'Ing. en Electronica y Telecomunicaciones'), (b'ING_CIV_IND', b'Ingenieria Civil Industrial'), (b'NUT', b'Nutricion y Dietetica'), (b'OBS', b'Obstetricia y Puericultura'), (b'PED_ED_DIF', b'Ped. en Educ. Diferencial m/DEA'), (b'PED_ED_FIS', b'Ped. en Educacion Fisica'), (b'PED_ED_GEN_BAS', b'Ped. en Educacion General Basica'), (b'PED_HIS', b'Ped. en Historia y Geografia'), (b'PED_ING', b'Ped. en Ingles'), (b'PED_LENG', b'Ped. en Lengua Castellana y Comunicacion'), (b'PED_MAT', b'Ped. en Matematica y Computacion'), (b'PED_MUS', b'Ped. en Musica m/ Educacion Extraescolar'), (b'PSICO', b'Psicologia'), (b'TEO', b'Teologia'), (b'TNS_ENF', b'TNS en Enfermeria'), (b'TRAB_SOC', b'Trabajo Social')])),
                ('tipo_Usuario', models.CharField(blank=True, max_length=25, choices=[(b'ADMINISTRATIVO', b'Administrativo'), (b'DECANO', b'Decano'), (b'DIR_CARRERA', b'Director de Carrera'), (b'SEC_ACAD', b'Secretario Academico')])),
                ('permiso', models.CharField(blank=True, max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3')])),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_reporte', models.CharField(blank=True, max_length=30, choices=[(b'Autoreporte', b'Autoreporte'), (b'Sigae', b'Sigae'), (b'Kolb', b'Kolb'), (b'Edward', b'Edward'), (b'Taller_Habilidades', b'Taller de Habilidades'), (b'Propedeutico', b'Propedeutico'), (b'Honey_Alonso', b'Honey Alonso'), (b'Tutores', b'Tutores'), (b'Ayudantias', b'Ayudantias')])),
                ('reporte_Departamento', models.CharField(blank=True, max_length=50, choices=[(b'FECS', b'Facultad de Educacion y Ciencias Sociales'), (b'FACS', b'Facultad de Ciencias de la Salud '), (b'FAIN', b'Facultad de Ingenieria y Negocios'), (b'FTEO', b'Facultad de Teologia'), (b'UNACH', b'Universidad Adventista de Chile'), (b'AGRO', b'Agronomia'), (b'CON_AUD', b'Contador Auditor'), (b'ED_PARV', b'Educacion Parvularia'), (b'ENF', b'Enfermeria'), (b'ING_CIV_INF', b'Ing. Civil en Informatica'), (b'ING_INF', b'Ing. Informatica'), (b'ING_COM', b'Ing. Comercial'), (b'ING_ELEC', b'Ing. en Electronica y Telecomunicaciones'), (b'ING_CIV_IND', b'Ingenieria Civil Industrial'), (b'NUT', b'Nutricion y Dietetica'), (b'OBS', b'Obstetricia y Puericultura'), (b'PED_BIO', b'Ped. en Biologia'), (b'PED_ED_DIF', b'Ped. en Educ. Diferencial m/DEA'), (b'PED_ED_FIS', b'Ped. en Educacion Fisica'), (b'PED_ED_GEN_BAS', b'Ped. en Educacion General Basica'), (b'PED_HIS', b'Ped. en Historia y Geografia'), (b'PED_ING', b'Ped. en Ingles'), (b'PED_LENG', b'Ped. en Lengua Castellana y Comunicacion'), (b'PED_MAT', b'Ped. en Matematica y Computacion'), (b'PED_MUS', b'Ped. en Musica m/ Educacion Extraescolar'), (b'PSICO', b'Psicologia'), (b'TEO', b'Teologia'), (b'TNS_ENF', b'TNS en Enfermeria'), (b'TRAB_SOC', b'Trabajo Social')])),
                ('ano_reporte', models.IntegerField(default=2015, blank=True)),
                ('fecha_publicacion', models.DateTimeField(null=True, blank=True)),
                ('reporte', models.FileField(null=True, upload_to=b'')),
            ],
        ),
    ]
