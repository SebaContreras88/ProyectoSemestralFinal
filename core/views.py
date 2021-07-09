from core.forms import ArteForm
from django.shortcuts import render, redirect
from .models import Arte
from .forms import ArteForm

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def iniciosesion(request):
    return render(request, 'core/iniciosesion.html')

def registrarse(request):
    return render(request, 'core/registrarse.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def manualidades(request):
    return render(request, 'core/manualidades.html')

def pinturas(request):
    return render(request,'core/pinturas.html')

def orfebreria(request):
    return render(request,'core/orfebreria.html')

def tejidos(request):
    return render(request,'core/tejidos.html')

def listaArtes(request):

    artes = Arte.objects.all()

    datos = {
        'artes' : artes
    }
    return render(request, 'core/listaArtes.html', datos)

def NuevaArte(request):

    form = ArteForm()

    datos = {
        'form' : form
    }

    if request.method == 'POST' :
        form = ArteForm(request.POST)
        if form.is_valid:
            form.save()
            datos['mensaje'] = '¡Arte Agregado Correctamente!'
    return render(request, 'core/nuevaArte.html', datos)

def editarArte(request,id):

    arte = Arte.objects.get(numarticulo=id)

    datos = {
        'form' : ArteForm(instance=arte)
    }
    
    if request.method =='POST':
        formulario = ArteForm(data=request.POST,instance=arte)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "¡Arte Modificado Correctamente!"
    return render(request, 'core/editarArte.html', datos)

def eliminarArte(request,id):
    arte = Arte.objects.get(numarticulo=id)

    arte.delete()

    return redirect(to="listaArtes")

