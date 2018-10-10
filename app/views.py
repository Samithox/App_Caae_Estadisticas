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
	if request.user.profile.permiso == 2:
			# Decano
		reports = Report.objects.filter(reporte_Facultad=request.user.profile.facultad,tipo_reporte='Autoreporte')

	elif request.user.profile.permiso == 3:
			# Director carrera
		reports = Report.objects.filter(carrera_reporte=request.user.profile.carrera,tipo_reporte='Autoreporte') 
	else:
		reports = Report.objects.filter(tipo_reporte='Autoreporte')
	return render(request, 'app/autoreporte.html',{'reports': reports})

@login_required
def kolb(request):
    return render(request, 'app/kolb.html',{})

@login_required
def edward(request):
    return render(request, 'app/edward.html',{})

@login_required
def tap(request):
    return render(request, 'app/tap.html',{}) 

@login_required
def sigae(request):
    return render(request, 'app/sigae.html',{})               
  

