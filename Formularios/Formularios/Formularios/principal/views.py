from django.shortcuts import redirect, render
from django.http import HttpResponse
from principal.models import Comuna
from principal.forms import ComunaForm

from . import forms

def listadoComunas(request):
    comunas= Comuna.objects.all()
    data={'comunas': comunas}
    return render(request, 'comunas.html', data)

def agregarComuna(request):
    form=forms.ComunaForm()
    if request.method == 'POST':
        form=ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return listadoComunas(request)
        data = {'form': form}
        return render(request, 'agregarcomunas.html', data)
    
def quitarComuna(request, id):
    comuna= Comuna.objects.get(id=id)
    comuna.delete()
    return redirect("/comunas")


def cambiarComuna(request, id):
    comuna= Comuna.objects.get(id=id)
    form= ComunaForm(instance=comuna)
    if request.method == 'POST':
        form= ComunaForm(request.POST, instance= comuna)
        if form.if_valid():
            form.save()
            return listadoComunas(request)
        data = {'form' : form}
        return render(request, 'agregarcomunas.html', data)
    
def buscarComuna(request, id):
    comuna= Comuna.objects.get(id=id)
    data= {'comunas' : comuna}
    return render(request, 'comunas.html', data)

