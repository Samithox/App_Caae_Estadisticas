from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Report(models.Model):
    nombre = models.CharField(max_length=50)
    AUTOREPORTE = 'Autoreporte'
    SIGAE = 'Sigae'
    KOLB = 'Kolb'
    EDWARD = 'Edward'
    TALL_HABILIDADES = 'Taller_Habilidades'
    PROPEDEUTICO = 'Propedeutico'
    HONEY_ALONSO = 'Honey_Alonso'
    TUTORES = 'Tutores'
    AYUDANTIAS = 'Ayudantias'
    TIPO_REPORTE_CHOICES = (
        (AUTOREPORTE,'Autoreporte'),
        (SIGAE,'Sigae'),
        (KOLB,'Kolb'),
        (EDWARD,'Edward'),
        (TALL_HABILIDADES,'Taller de Habilidades'),
        (PROPEDEUTICO,'Propedeutico'),
        (HONEY_ALONSO,'Honey Alonso'),
        (TUTORES,'Tutores'),
        (AYUDANTIAS,'Ayudantias'),
        )
    tipo_reporte = models.CharField(max_length=30,choices=TIPO_REPORTE_CHOICES,blank=True)
    FACULTAD_DE_EDUCACION = 'FECS'
    FACULTAD_DE_SALUD = 'FACS'
    FACULTAD_INGENIERIA = 'FAIN'
    FACULTAD_TEOLOGIA = 'FTEO'
    UNIVERSIDAD = 'UNACH'
    AGRONOMIA='AGRO'
    CONTADOR_AUDITOR='CON_AUD'
    ED_PARVULARIA='ED_PARV'
    ENFERMERIA='ENF'
    ING_CIVIL_INFORMATICA='ING_CIV_INF'
    ING_INFORMATICA='ING_INF'
    ING_COMERCIAL='ING_COM'
    ING_ELECTRONICA='ING_ELEC'
    ING_CIVIL_INDUSTRIAL='ING_CIV_IND'
    NUTRICION='NUT'
    OBSTETRICIA='OBS'
    PED_BIO = 'PED_BIO'
    PED_ED_DIFERENCIAL='PED_ED_DIF'
    PED_ED_FISICA='PED_ED_FIS'
    PED_ED_GEN_BASICA='PED_ED_GEN_BAS'
    PED_HISTORIA='PED_HIS'
    PED_INGLES='PED_ING'
    PED_LENGUAJE='PED_LENG'
    PED_MATEMATICA='PED_MAT'
    PED_MUSICA='PED_MUS'
    PSICOLOGIA='PSICO'
    TEOLOGIA='TEO'
    TNS_ENFERMERIA='TNS_ENF'
    TRABAJO_SOCIAL='TRAB_SOC'
    FACULTAD_REPORTS_CHOICES =(
        (FACULTAD_DE_EDUCACION,'Facultad de Educacion y Ciencias Sociales'),
        (FACULTAD_DE_SALUD,'Facultad de Ciencias de la Salud '),
        (FACULTAD_INGENIERIA,'Facultad de Ingenieria y Negocios'),
        (FACULTAD_TEOLOGIA,'Facultad de Teologia'),
        (UNIVERSIDAD,'Universidad Adventista de Chile'),
        (AGRONOMIA,'Agronomia'),
        (CONTADOR_AUDITOR,'Contador Auditor'),
        (ED_PARVULARIA,'Educacion Parvularia'),
        (ENFERMERIA,'Enfermeria'),
        (ING_CIVIL_INFORMATICA,'Ing. Civil en Informatica'),
        (ING_INFORMATICA,'Ing. Informatica'),
        (ING_COMERCIAL,'Ing. Comercial'),
        (ING_ELECTRONICA,'Ing. en Electronica y Telecomunicaciones'),
        (ING_CIVIL_INDUSTRIAL,'Ingenieria Civil Industrial'),
        (NUTRICION,'Nutricion y Dietetica'),
        (OBSTETRICIA,'Obstetricia y Puericultura'),
        (PED_BIO,'Ped. en Biologia'),
        (PED_ED_DIFERENCIAL,'Ped. en Educ. Diferencial m/DEA'),
        (PED_ED_FISICA,'Ped. en Educacion Fisica'),
        (PED_ED_GEN_BASICA,'Ped. en Educacion General Basica'),
        (PED_HISTORIA,'Ped. en Historia y Geografia'),
        (PED_INGLES,'Ped. en Ingles'),
        (PED_LENGUAJE,'Ped. en Lengua Castellana y Comunicacion'),
        (PED_MATEMATICA,'Ped. en Matematica y Computacion'),
        (PED_MUSICA,'Ped. en Musica m/ Educacion Extraescolar'),
        (PSICOLOGIA,'Psicologia'),
        (TEOLOGIA,'Teologia'),
        (TNS_ENFERMERIA,'TNS en Enfermeria'),
        (TRABAJO_SOCIAL,'Trabajo Social'),
        )
    reporte_Departamento = models.CharField(max_length=50,choices=FACULTAD_REPORTS_CHOICES,blank=True)
    ano_reporte = models.IntegerField(blank=True,default=2015)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    reporte = models.FileField(null=True)
    objects  = models.Manager()

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return '%s_%s_%s' % (self.ano_reporte, self.tipo_reporte,self.nombre)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    FACULTAD_DE_EDUCACION = 'FECS'
    FACULTAD_DE_SALUD = 'FACS'
    FACULTAD_INGENIERIA = 'FAIN'
    FACULTAD_TEOLOGIA = 'FTEO'
    UNIVERSIDAD = 'UNACH'
    FACULTAD_CHOICES =(
        (FACULTAD_DE_EDUCACION,'Facultad de Educacion y Ciencias Sociales'),
        (FACULTAD_DE_SALUD,'Facultad de Ciencias de la Salud'),
        (FACULTAD_INGENIERIA,'Facultad de Ingenieria y Negocios'),
        (FACULTAD_TEOLOGIA,'Facultad de Teologia'),
        (UNIVERSIDAD,'Universidad Adventista de Chile'),
        )
    facultad = models.CharField(max_length=5,choices=FACULTAD_CHOICES,blank=True)
    TODAS='ALL'
    AGRONOMIA='AGRO'
    CONTADOR_AUDITOR='CON_AUD'
    ED_PARVULARIA='ED_PARV'
    ENFERMERIA='ENF'
    ING_CIVIL_INFORMATICA='ING_CIV_INF'
    ING_COMERCIAL='ING_COM'
    ING_ELECTRONICA='ING_ELEC'
    ING_CIVIL_INDUSTRIAL='ING_CIV_IND'
    NUTRICION='NUT'
    OBSTETRICIA='OBS'
    PED_ED_DIFERENCIAL='PED_ED_DIF'
    PED_ED_FISICA='PED_ED_FIS'
    PED_ED_GEN_BASICA='PED_ED_GEN_BAS'
    PED_HISTORIA='PED_HIS'
    PED_INGLES='PED_ING'
    PED_LENGUAJE='PED_LENG'
    PED_MATEMATICA='PED_MAT'
    PED_MUSICA='PED_MUS'
    PSICOLOGIA='PSICO'
    TEOLOGIA='TEO'
    TNS_ENFERMERIA='TNS_ENF'
    TRABAJO_SOCIAL='TRAB_SOC'
    CARRERAS_CHOICE = (
        (TODAS,'Todas'),
        (AGRONOMIA,'Agronomia'),
        (CONTADOR_AUDITOR,'Contador Auditor'),
        (ED_PARVULARIA,'Educacion Parvularia'),
        (ENFERMERIA,'Enfermeria'),
        (ING_CIVIL_INFORMATICA,'Ing. Civil en Informatica'),
        (ING_COMERCIAL,'Ing. Comercial'),
        (ING_ELECTRONICA,'Ing. en Electronica y Telecomunicaciones'),
        (ING_CIVIL_INDUSTRIAL,'Ingenieria Civil Industrial'),
        (NUTRICION,'Nutricion y Dietetica'),
        (OBSTETRICIA,'Obstetricia y Puericultura'),
        (PED_ED_DIFERENCIAL,'Ped. en Educ. Diferencial m/DEA'),
        (PED_ED_FISICA,'Ped. en Educacion Fisica'),
        (PED_ED_GEN_BASICA,'Ped. en Educacion General Basica'),
        (PED_HISTORIA,'Ped. en Historia y Geografia'),
        (PED_INGLES,'Ped. en Ingles'),
        (PED_LENGUAJE,'Ped. en Lengua Castellana y Comunicacion'),
        (PED_MATEMATICA,'Ped. en Matematica y Computacion'),
        (PED_MUSICA,'Ped. en Musica m/ Educacion Extraescolar'),
        (PSICOLOGIA,'Psicologia'),
        (TEOLOGIA,'Teologia'),
        (TNS_ENFERMERIA,'TNS en Enfermeria'),
        (TRABAJO_SOCIAL,'Trabajo Social'),
        )
    carrera = models.CharField(max_length=50,choices=CARRERAS_CHOICE,blank=True)
    ADMINISTRATIVO = 'ADMINISTRATIVO'
    DECANO = 'DECANO'
    DIR_CARRERA = 'DIR_CARRERA'
    SEC_ACAD = 'SEC_ACAD'
    TIPO_USUARIO_CHOICE =(
        (ADMINISTRATIVO,'Administrativo'),
        (DECANO,'Decano'),
        (DIR_CARRERA,'Director de Carrera'),
        (SEC_ACAD,'Secretario Academico'),
        )
    tipo_Usuario = models.CharField(max_length=25,choices=TIPO_USUARIO_CHOICE,blank=True)
    NIVEL_1 = '1'
    NIVEL_2 = '2'
    NIVEL_3 = '3'
    PERMISO_CHOICE = (
        (NIVEL_1,'1'),
        (NIVEL_2,'2'),
        (NIVEL_3,'3'),
        )
    permiso = models.CharField(max_length=1,choices=PERMISO_CHOICE,blank=True)
    MASCULINO = 'M'
    FEMENINO = 'F'
    SEXO_CHOICE = (
        (MASCULINO,'Masculino'),
        (FEMENINO,'Femenino'),
        )
    sexo = models.CharField(max_length=1,choices=SEXO_CHOICE,blank=True) 

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ('facultad','carrera','tipo_Usuario','permiso')
    AUTH_PROFILE_MODULE = 'app.Profile'
    
    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


