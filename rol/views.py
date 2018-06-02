from django.shortcuts import render, redirect
from .models import empleado, afiliado, registro
# Create your views here.
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .forms import empleadoForm, afiliadoForm, registroForm

def principal(request):
    return render(request, 'index.html')

#registro
class vistaRegistro(CreateView):
	template_name = 'registro.html'
	form_class = registroForm
	success_url = 'listaRegistro'

class listaRegistro(ListView):
	template_name = 'listaRegistro.html'
	model = registro

	def get_queryset(self):
		return registro.objects.all()

class editarRegistro(UpdateView):
	template_name = 'Registro.html'
	model = registro
	form_class = registroForm
	success_url = 'listaRegistro'

class eliminarRegistro(DeleteView):
	template_name = 'eliminar.html'
	model = registro
	success_url = 'listaRegistro'
#end registro

#start empleado
def create_empleado(request):
    if request.method == 'POST':
        formulario = empleadoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleado_list')
    else:
        formulario = empleadoForm()
    return render(request, 'empleado.html', {'formulario': formulario})

def empleado_list(request):
    empleado_list = empleado.objects.all()
    return render(request, 'empleado_list.html', {'empleado_list': empleado_list})
#end empleado

#start afiliado
def create_afiliado(request):
    if request.method == 'POST':
        formulario = afiliadoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('afiliado_list')
    else:
        formulario = afiliadoForm()
    return render(request, 'afiliado.html', {'formulario': formulario})

def afiliado_list(request):
    afiliado_list = afiliado.objects.all()
    return render(request, 'afiliado_list.html', {'afiliado_list': afiliado_list})
#end afiliado

#filtros por lugar
def registro_comitancillo(request):
    profile_list = registro.objects.filter(lugar = 'Comitancillo')
    return render(request, 'listaRegistro.html', {'object_list': profile_list})

def registro_lorenzo(request):
    profile_list = registro.objects.filter(lugar = 'San Lorenzo')
    return render(request, 'listaRegistro.html', {'object_list': profile_list})
#fin filtros por lugar

#filtros por tratamiento
def registro_relleno(request):
    profile_list = registro.objects.filter(tratamiento = 'Rellenos')
    return render(request, 'listaRegistro.html', {'object_list': profile_list})

def registro_canales(request):
    profile_list = registro.objects.filter(tratamiento = 'T. de canales')
    return render(request, 'listaRegistro.html', {'object_list': profile_list})

def registro_limpieza(request):
    profile_list = registro.objects.filter(tratamiento = 'Limpieza')
    return render(request, 'listaRegistro.html', {'object_list': profile_list})

def registro_extraccion(request):
    profile_list = registro.objects.filter(tratamiento = 'Extraccion')
    return render(request, 'listaRegistro.html', {'object_list': profile_list})
#fin filtros por tratamiento