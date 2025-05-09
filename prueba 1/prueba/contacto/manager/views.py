from django.shortcuts import render, get_object_or_404, redirect
from .models import Contacto
from .forms import ContactoForm

def listar_contactos(request):
    contactos = Contacto.objects.filter(eliminado=False)
    return render(request, 'agenda/listar.html', {'contactos': contactos})

def detalle_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    return render(request, 'agenda/detalle.html', {'contacto': contacto})

def crear_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contactos')
    else:
        form = ContactoForm()
    return render(request, 'agenda/formulario.html', {'form': form})

def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('listar_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'agenda/formulario.html', {'form': form})

def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    contacto.eliminado = True
    contacto.save()
    return redirect('listar_contactos')
