from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'app/reportes.html',{})

@login_required
def inicio(request):
    return render(request, 'app/index.html',{})

@login_required
def autoreporte(request):
    return render(request, 'app/autoreporte.html',{})

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
  

