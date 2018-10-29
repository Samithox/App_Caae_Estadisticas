from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .mixins import user_test_nivel_one
from .models import Profile, Report

# Create your views here.
@login_required
#@user_passes_test(user_test_nivel_one)
def home(request):
	return render(request, 'app/reportes.html',{})

@login_required
def inicio(request):
    return render(request, 'app/index.html',{})

@login_required
def autoreporte(request):
	if request.user.profile.permiso == '2':
		if request.user.profile.facultad == 'FECS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ED_PARV','PED_BIO','PED_ED_DIF','PED_ED_FIS','PED_ED_GEN_BAS','PED_HIS','PED_ING','PED_LENG','PED_MAT','PED_MUS','TRAB_SOC'],tipo_reporte='Autoreporte').order_by('nombre')
		elif request.user.profile.facultad == 'FACS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ENF','NUT','OBS','PSICO','TNS_ENF'],tipo_reporte='Autoreporte').order_by('nombre')
		elif request.user.profile.facultad == 'FAIN':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO','CON_AUD','ING_CIV_INF','ING_COM','ING_ELEC','ING_CIV_IND','ING_INF'],tipo_reporte='Autoreporte').order_by('nombre')
		elif request.user.profile.facultad == 'FTEO':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FTEO','TEO'],tipo_reporte='Autoreporte').order_by('nombre')	
	elif request.user.profile.permiso == '3':
		if request.user.profile.carrera == 'AGRO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO'], tipo_reporte='Autoreporte').order_by('nombre')
		elif request.user.profile.carrera == 'CON_AUD':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','CON_AUD'], tipo_reporte='Autoreporte').order_by('nombre')
		elif request.user.profile.carrera == 'ED_PARV':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ED_PARV'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ENF'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_INF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_INF','ING_INF'], tipo_reporte='Autoreporte').order_by('nombre')
		elif request.user.profile.carrera == 'ING_COM':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_COM','CON_AUD'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_ELEC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_ELEC'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_IND':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_IND'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'NUT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','NUT'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'OBS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','OBS'], tipo_reporte='Autoreporte').order_by('nombre')
		elif request.user.profile.carrera == 'PED_ED_DIF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_DIF'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_BIO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_BIO'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_FIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_FIS'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_GEN_BAS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_GEN_BAS'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_HIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_HIS'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ING':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ING'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_LENG':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_LENG'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MAT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MAT'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MUS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MUS'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'PSICO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PSICO'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'TEO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TEO'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'TNS_ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TNS_ENF'], tipo_reporte='Autoreporte').order_by('nombre') 
		elif request.user.profile.carrera == 'TRAB_SOC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TRAB_SOC'], tipo_reporte='Autoreporte').order_by('nombre')   
	elif request.user.profile.permiso == '1':
		reports = Report.objects.filter(tipo_reporte='Autoreporte').order_by('nombre')
	else:
		reports = Report.objects.none()
	return render(request, 'app/autoreporte.html',{'reports': reports})

@login_required
def kolb(request):
	if request.user.profile.permiso == '2':
		if request.user.profile.facultad == 'FECS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ED_PARV','PED_BIO','PED_ED_DIF','PED_ED_FIS','PED_ED_GEN_BAS','PED_HIS','PED_ING','PED_LENG','PED_MAT','PED_MUS','TRAB_SOC'],tipo_reporte='Kolb').order_by('nombre')
		elif request.user.profile.facultad == 'FACS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ENF','NUT','OBS','PSICO','TNS_ENF'],tipo_reporte='Kolb').order_by('nombre')
		elif request.user.profile.facultad == 'FAIN':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO','CON_AUD','ING_CIV_INF','ING_COM','ING_ELEC','ING_CIV_IND','ING_INF'],tipo_reporte='Kolb').order_by('nombre')
		elif request.user.profile.facultad == 'FTEO':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FTEO','TEO'],tipo_reporte='Kolb').order_by('nombre')
	elif request.user.profile.permiso == '3':
		if request.user.profile.carrera == 'AGRO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO'], tipo_reporte='Kolb').order_by('nombre')
		elif request.user.profile.carrera == 'CON_AUD':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','CON_AUD'], tipo_reporte='Kolb').order_by('nombre')
		elif request.user.profile.carrera == 'ED_PARV':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ED_PARV'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ENF'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_INF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_INF','ING_INF'], tipo_reporte='Kolb').order_by('nombre')
		elif request.user.profile.carrera == 'ING_COM':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_COM','CON_AUD'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_ELEC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_ELEC'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_IND':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_IND'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'NUT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','NUT'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'OBS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','OBS'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_DIF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_DIF'], tipo_reporte='Kolb').order_by('nombre')
		elif request.user.profile.carrera == 'PED_BIO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_BIO'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_FIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_FIS'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_GEN_BAS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_GEN_BAS'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_HIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_HIS'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ING':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ING'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_LENG':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_LENG'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MAT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MAT'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MUS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MUS'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'PSICO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PSICO'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'TEO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TEO'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'TNS_ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TNS_ENF'], tipo_reporte='Kolb').order_by('nombre') 
		elif request.user.profile.carrera == 'TRAB_SOC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TRAB_SOC'], tipo_reporte='Kolb').order_by('nombre')   
	elif request.user.profile.permiso == '1':
		reports = Report.objects.filter(tipo_reporte='Kolb').order_by('nombre')
	else: 
		reports = Report.objects.none()
	return render(request, 'app/kolb.html',{'reports': reports})

@login_required
def edward(request):
	if request.user.profile.permiso == '2':
		if request.user.profile.facultad == 'FECS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ED_PARV','PED_BIO','PED_ED_DIF','PED_ED_FIS','PED_ED_GEN_BAS','PED_HIS','PED_ING','PED_LENG','PED_MAT','PED_MUS','TRAB_SOC'],tipo_reporte='Edward').order_by('nombre')
		elif request.user.profile.facultad == 'FACS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ENF','NUT','OBS','PSICO','TNS_ENF'],tipo_reporte='Edward').order_by('nombre')
		elif request.user.profile.facultad == 'FAIN':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO','CON_AUD','ING_CIV_INF','ING_COM','ING_ELEC','ING_CIV_IND','ING_INF'],tipo_reporte='Edward').order_by('nombre')
		elif request.user.profile.facultad == 'FTEO':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FTEO','TEO'],tipo_reporte='Edward').order_by('nombre')
	elif request.user.profile.permiso == '3':
		if request.user.profile.carrera == 'AGRO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO'], tipo_reporte='Edward').order_by('nombre')
		elif request.user.profile.carrera == 'CON_AUD':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','CON_AUD'], tipo_reporte='Edward').order_by('nombre')
		elif request.user.profile.carrera == 'ED_PARV':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ED_PARV'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ENF'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_INF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_INF','ING_INF'], tipo_reporte='Edward').order_by('nombre')
		elif request.user.profile.carrera == 'ING_COM':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_COM','CON_AUD'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_ELEC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_ELEC'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_IND':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_IND'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'NUT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','NUT'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'OBS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','OBS'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_DIF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_DIF'], tipo_reporte='Edward').order_by('nombre')
		elif request.user.profile.carrera == 'PED_BIO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_BIO'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_FIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_FIS'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_GEN_BAS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_GEN_BAS'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_HIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_HIS'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ING':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ING'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_LENG':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_LENG'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MAT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MAT'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MUS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MUS'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'PSICO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PSICO'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'TEO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TEO'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'TNS_ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TNS_ENF'], tipo_reporte='Edward').order_by('nombre') 
		elif request.user.profile.carrera == 'TRAB_SOC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TRAB_SOC'], tipo_reporte='Edward').order_by('nombre')
	elif request.user.profile.permiso == '1':
		reports = Report.objects.filter(tipo_reporte='Edward').order_by('nombre')
	else: 
		reports = Report.objects.none()
	return render(request, 'app/edward.html',{'reports': reports})

@login_required
def tap(request):
	if request.user.profile.permiso == '2':
		if request.user.profile.facultad == 'FECS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ED_PARV','PED_BIO','PED_ED_DIF','PED_ED_FIS','PED_ED_GEN_BAS','PED_HIS','PED_ING','PED_LENG','PED_MAT','PED_MUS','TRAB_SOC'],tipo_reporte='Taller de Habilidades').order_by('nombre')
		elif request.user.profile.facultad == 'FACS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ENF','NUT','OBS','PSICO','TNS_ENF'],tipo_reporte='Taller de Habilidades').order_by('nombre')
		elif request.user.profile.facultad == 'FAIN':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO','CON_AUD','ING_CIV_INF','ING_COM','ING_ELEC','ING_CIV_IND','ING_INF'],tipo_reporte='Taller de Habilidades').order_by('nombre')
		elif request.user.profile.facultad == 'FTEO':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FTEO','TEO'],tipo_reporte='Taller de Habilidades').order_by('nombre')
	elif request.user.profile.permiso == '3':
		if request.user.profile.carrera == 'AGRO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO'], tipo_reporte='Taller de Habilidades').order_by('nombre')
		elif request.user.profile.carrera == 'CON_AUD':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','CON_AUD'], tipo_reporte='Taller de Habilidades').order_by('nombre')
		elif request.user.profile.carrera == 'ED_PARV':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ED_PARV'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ENF'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_INF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_INF','ING_INF'], tipo_reporte='Taller de Habilidades').order_by('nombre')
		elif request.user.profile.carrera == 'ING_COM':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_COM','CON_AUD'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_ELEC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_ELEC'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_IND':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_IND'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'NUT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','NUT'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'OBS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','OBS'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_DIF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_DIF'], tipo_reporte='Taller de Habilidades').order_by('nombre')
		elif request.user.profile.carrera == 'PED_BIO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_BIO'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_FIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_FIS'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_GEN_BAS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_GEN_BAS'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_HIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_HIS'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ING':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ING'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_LENG':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_LENG'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MAT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MAT'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MUS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MUS'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'PSICO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PSICO'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'TEO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TEO'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'TNS_ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TNS_ENF'], tipo_reporte='Taller de Habilidades').order_by('nombre') 
		elif request.user.profile.carrera == 'TRAB_SOC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TRAB_SOC'], tipo_reporte='Taller de Habilidades').order_by('nombre')
	elif request.user.profile.permiso == '1':
		reports = Report.objects.filter(tipo_reporte='Taller de Habilidades').order_by('nombre')
	else: 
		reports = Report.objects.none()
	return render(request, 'app/tap.html',{'reports': reports}) 

@login_required
def sigae(request):
	if request.user.profile.permiso == '2':
		if request.user.profile.facultad == 'FECS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ED_PARV','PED_BIO','PED_ED_DIF','PED_ED_FIS','PED_ED_GEN_BAS','PED_HIS','PED_ING','PED_LENG','PED_MAT','PED_MUS','TRAB_SOC'],tipo_reporte='Sigae').order_by('nombre')
		elif request.user.profile.facultad == 'FACS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ENF','NUT','OBS','PSICO','TNS_ENF'],tipo_reporte='Sigae').order_by('nombre')
		elif request.user.profile.facultad == 'FAIN':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO','CON_AUD','ING_CIV_INF','ING_COM','ING_ELEC','ING_CIV_IND','ING_INF'],tipo_reporte='Sigae').order_by('nombre')
		elif request.user.profile.facultad == 'FTEO':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FTEO','TEO'],tipo_reporte='Sigae').order_by('nombre')
	elif request.user.profile.permiso == '3':
		if request.user.profile.carrera == 'AGRO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO'], tipo_reporte='Sigae').order_by('nombre')
		elif request.user.profile.carrera == 'CON_AUD':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','CON_AUD'], tipo_reporte='Sigae').order_by('nombre')
		elif request.user.profile.carrera == 'ED_PARV':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ED_PARV'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ENF'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_INF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_INF','ING_INF'], tipo_reporte='Sigae').order_by('nombre')
		elif request.user.profile.carrera == 'ING_COM':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_COM','CON_AUD'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_ELEC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_ELEC'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_IND':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_IND'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'NUT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','NUT'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'OBS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','OBS'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_DIF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_DIF'], tipo_reporte='Sigae').order_by('nombre')
		elif request.user.profile.carrera == 'PED_BIO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_BIO'], tipo_reporte='Sigae').order_by('nombre')
		elif request.user.profile.carrera == 'PED_ED_FIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_FIS'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_GEN_BAS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_GEN_BAS'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_HIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_HIS'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ING':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ING'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_LENG':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_LENG'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MAT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MAT'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MUS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MUS'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'PSICO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PSICO'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'TEO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TEO'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'TNS_ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TNS_ENF'], tipo_reporte='Sigae').order_by('nombre') 
		elif request.user.profile.carrera == 'TRAB_SOC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TRAB_SOC'], tipo_reporte='Sigae').order_by('nombre')
	elif request.user.profile.permiso == '1':
		reports = Report.objects.filter(tipo_reporte='Sigae').order_by('nombre')
	else: 
		reports = Report.objects.none()
	return render(request, 'app/sigae.html',{'reports': reports})               
  
@login_required
def propedeutico(request):
	if request.user.profile.permiso == '2':
		if request.user.profile.facultad == 'FECS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ED_PARV','PED_BIO','PED_ED_DIF','PED_ED_FIS','PED_ED_GEN_BAS','PED_HIS','PED_ING','PED_LENG','PED_MAT','PED_MUS','TRAB_SOC'],tipo_reporte='Propedeutico').order_by('nombre')
		elif request.user.profile.facultad == 'FACS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ENF','NUT','OBS','PSICO','TNS_ENF'],tipo_reporte='Propedeutico').order_by('nombre')
		elif request.user.profile.facultad == 'FAIN':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO','CON_AUD','ING_CIV_INF','ING_COM','ING_ELEC','ING_CIV_IND','ING_INF'],tipo_reporte='Propedeutico').order_by('nombre')
		elif request.user.profile.facultad == 'FTEO':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FTEO','TEO'],tipo_reporte='Propedeutico').order_by('nombre')
	elif request.user.profile.permiso == '3':
		if request.user.profile.carrera == 'AGRO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO'], tipo_reporte='Propedeutico').order_by('nombre')
		elif request.user.profile.carrera == 'CON_AUD':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','CON_AUD'], tipo_reporte='Propedeutico').order_by('nombre')
		elif request.user.profile.carrera == 'ED_PARV':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ED_PARV'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ENF'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_INF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_INF','ING_INF'], tipo_reporte='Propedeutico').order_by('nombre')
		elif request.user.profile.carrera == 'ING_COM':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_COM','CON_AUD'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_ELEC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_ELEC'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_IND':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_IND'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'NUT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','NUT'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'OBS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','OBS'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_DIF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_DIF'], tipo_reporte='Propedeutico').order_by('nombre')
		elif request.user.profile.carrera == 'PED_BIO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_BIO'], tipo_reporte='Propedeutico').order_by('nombre')
		elif request.user.profile.carrera == 'PED_ED_FIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_FIS'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_GEN_BAS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_GEN_BAS'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_HIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_HIS'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ING':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ING'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_LENG':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_LENG'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MAT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MAT'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MUS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MUS'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'PSICO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PSICO'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'TEO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TEO'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'TNS_ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TNS_ENF'], tipo_reporte='Propedeutico').order_by('nombre') 
		elif request.user.profile.carrera == 'TRAB_SOC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TRAB_SOC'], tipo_reporte='Propedeutico').order_by('nombre')
	elif request.user.profile.permiso == '1':
		reports = Report.objects.filter(tipo_reporte='Propedeutico').order_by('nombre')
	else: 
		reports = Report.objects.none()
	return render(request, 'app/propedeutico.html',{'reports': reports})

@login_required
def honeyalonso(request):
	if request.user.profile.permiso == '2':
		if request.user.profile.facultad == 'FECS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ED_PARV','PED_BIO','PED_ED_DIF','PED_ED_FIS','PED_ED_GEN_BAS','PED_HIS','PED_ING','PED_LENG','PED_MAT','PED_MUS','TRAB_SOC'],tipo_reporte='Honey Alonso').order_by('nombre')
		elif request.user.profile.facultad == 'FACS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ENF','NUT','OBS','PSICO','TNS_ENF'],tipo_reporte='Honey Alonso').order_by('nombre')
		elif request.user.profile.facultad == 'FAIN':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO','CON_AUD','ING_CIV_INF','ING_COM','ING_ELEC','ING_CIV_IND','ING_INF'],tipo_reporte='Honey Alonso').order_by('nombre')
		elif request.user.profile.facultad == 'FTEO':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FTEO','TEO'],tipo_reporte='Honey Alonso').order_by('nombre')
	elif request.user.profile.permiso == '3':
		if request.user.profile.carrera == 'AGRO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO'], tipo_reporte='Honey Alonso').order_by('nombre')
		elif request.user.profile.carrera == 'CON_AUD':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','CON_AUD'], tipo_reporte='Honey Alonso').order_by('nombre')
		elif request.user.profile.carrera == 'ED_PARV':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ED_PARV'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ENF'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_INF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_INF','ING_INF'], tipo_reporte='Honey Alonso').order_by('nombre')
		elif request.user.profile.carrera == 'ING_COM':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_COM','CON_AUD'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_ELEC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_ELEC'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_IND':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_IND'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'NUT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','NUT'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'OBS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','OBS'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_DIF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_DIF'], tipo_reporte='Honey Alonso').order_by('nombre')
		elif request.user.profile.carrera == 'PED_BIO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_BIO'], tipo_reporte='Honey Alonso').order_by('nombre')
		elif request.user.profile.carrera == 'PED_ED_FIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_FIS'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_GEN_BAS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_GEN_BAS'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_HIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_HIS'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ING':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ING'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_LENG':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_LENG'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MAT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MAT'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MUS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MUS'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'PSICO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PSICO'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'TEO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TEO'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'TNS_ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TNS_ENF'], tipo_reporte='Honey Alonso').order_by('nombre') 
		elif request.user.profile.carrera == 'TRAB_SOC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TRAB_SOC'], tipo_reporte='Honey Alonso').order_by('nombre')
	elif request.user.profile.permiso == '1':
		reports = Report.objects.filter(tipo_reporte='Honey Alonso').order_by('nombre')
	else: 
		reports = Report.objects.none()
	return render(request, 'app/honeyalonso.html',{'reports': reports})

@login_required
def tutores(request):
	if request.user.profile.permiso == '2':
		if request.user.profile.facultad == 'FECS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ED_PARV','PED_BIO','PED_ED_DIF','PED_ED_FIS','PED_ED_GEN_BAS','PED_HIS','PED_ING','PED_LENG','PED_MAT','PED_MUS','TRAB_SOC'],tipo_reporte='Tutores').order_by('nombre')
		elif request.user.profile.facultad == 'FACS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ENF','NUT','OBS','PSICO','TNS_ENF'],tipo_reporte='Tutores').order_by('nombre')
		elif request.user.profile.facultad == 'FAIN':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO','CON_AUD','ING_CIV_INF','ING_COM','ING_ELEC','ING_CIV_IND','ING_INF'],tipo_reporte='Tutores').order_by('nombre')
		elif request.user.profile.facultad == 'FTEO':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FTEO','TEO'],tipo_reporte='Tutores').order_by('nombre')
	elif request.user.profile.permiso == '3':
		if request.user.profile.carrera == 'AGRO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO'], tipo_reporte='Tutores').order_by('nombre')
		elif request.user.profile.carrera == 'CON_AUD':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','CON_AUD'], tipo_reporte='Tutores').order_by('nombre')
		elif request.user.profile.carrera == 'ED_PARV':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ED_PARV'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ENF'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_INF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_INF','ING_INF'], tipo_reporte='Tutores').order_by('nombre')
		elif request.user.profile.carrera == 'ING_COM':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_COM','CON_AUD'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_ELEC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_ELEC'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_IND':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_IND'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'NUT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','NUT'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'OBS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','OBS'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_DIF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_DIF'], tipo_reporte='Tutores').order_by('nombre')
		elif request.user.profile.carrera == 'PED_BIO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_BIO'], tipo_reporte='Tutores').order_by('nombre')
		elif request.user.profile.carrera == 'PED_ED_FIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_FIS'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_GEN_BAS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_GEN_BAS'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_HIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_HIS'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ING':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ING'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_LENG':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_LENG'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MAT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MAT'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MUS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MUS'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'PSICO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PSICO'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'TEO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TEO'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'TNS_ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TNS_ENF'], tipo_reporte='Tutores').order_by('nombre') 
		elif request.user.profile.carrera == 'TRAB_SOC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TRAB_SOC'], tipo_reporte='Tutores').order_by('nombre')
	elif request.user.profile.permiso == '1':
		reports = Report.objects.filter(tipo_reporte='Tutores').order_by('nombre')
	else: 
		reports = Report.objects.none()
	return render(request, 'app/tutores.html',{'reports': reports})

@login_required
def ayudantias(request):
	if request.user.profile.permiso == '2':
		if request.user.profile.facultad == 'FECS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ED_PARV','PED_BIO','PED_ED_DIF','PED_ED_FIS','PED_ED_GEN_BAS','PED_HIS','PED_ING','PED_LENG','PED_MAT','PED_MUS','TRAB_SOC'],tipo_reporte='Ayudantias').order_by('nombre')
		elif request.user.profile.facultad == 'FACS':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FACS','ENF','NUT','OBS','PSICO','TNS_ENF'],tipo_reporte='Ayudantias').order_by('nombre')
		elif request.user.profile.facultad == 'FAIN':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO','CON_AUD','ING_CIV_INF','ING_COM','ING_ELEC','ING_CIV_IND','ING_INF'],tipo_reporte='Ayudantias').order_by('nombre')
		elif request.user.profile.facultad == 'FTEO':
			reports = Report.objects.filter(reporte_Departamento__in=['UNACH','FTEO','TEO'],tipo_reporte='Ayudantias').order_by('nombre')
	elif request.user.profile.permiso == '3':
		if request.user.profile.carrera == 'AGRO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','AGRO'], tipo_reporte='Ayudantias').order_by('nombre')
		elif request.user.profile.carrera == 'CON_AUD':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','CON_AUD'], tipo_reporte='Ayudantias').order_by('nombre')
		elif request.user.profile.carrera == 'ED_PARV':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ED_PARV'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ENF'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_INF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_INF','ING_INF'], tipo_reporte='Ayudantias').order_by('nombre')
		elif request.user.profile.carrera == 'ING_COM':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_COM','CON_AUD'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_ELEC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_ELEC'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'ING_CIV_IND':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','ING_CIV_IND'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'NUT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','NUT'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'OBS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','OBS'], tipo_reporte='Ayudantias').order_by('nombre')
		elif request.user.profile.carrera == 'PED_BIO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_BIO'], tipo_reporte='Ayudantias').order_by('nombre')
		elif request.user.profile.carrera == 'PED_ED_DIF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_DIF'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_FIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_FIS'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ED_GEN_BAS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ED_GEN_BAS'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_HIS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_HIS'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_ING':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_ING'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_LENG':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_LENG'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MAT':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MAT'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'PED_MUS':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PED_MUS'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'PSICO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','PSICO'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'TEO':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TEO'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'TNS_ENF':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TNS_ENF'], tipo_reporte='Ayudantias').order_by('nombre') 
		elif request.user.profile.carrera == 'TRAB_SOC':
			reports = Report.objects.filter(reporte_Departamento__in=['FAIN','UNACH','TRAB_SOC'], tipo_reporte='Ayudantias').order_by('nombre')
	elif request.user.profile.permiso == '1':
		reports = Report.objects.filter(tipo_reporte='Ayudantias').order_by('nombre')
	else: 
		reports = Report.objects.none()
	return render(request, 'app/ayudantias.html',{'reports': reports})