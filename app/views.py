from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .mixins import user_test_nivel_one
from .models import Cliente
from .forms import ClienteForm
from django.shortcuts import redirect

# Create your views here.
@login_required
#@user_passes_test(user_test_nivel_one)
def home(request):
	clientes = Cliente.objects.all().order_by('rut_Cliente')

	return render(request, 'app/reportes.html',{'clientes': clientes})

@login_required
def inicio(request):
    return render(request, 'app/index.html',{})

@login_required
def ingresarClientes(request):
	form = "Dummy String"
	form_class = ClienteForm
	form = form_class(request.POST )
	
	if request.method == "POST":
		if form.is_valid():
			cliente = form.save(commit=False)
			cliente.save()
			return redirect('app.views.ingresarClientes')
	
		
    
	
	return render(request, 'app/ingresarClientes.html',{'form': form})

