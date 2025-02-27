from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})

def agregar_tarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        if titulo:
            Tarea.objects.create(titulo=titulo, descripcion=descripcion)
            return redirect('lista_tareas')
    return render(request, 'tareas/agregar_tarea.html')

def marcar_completada(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.completada = True
    tarea.save()
    return redirect('lista_tareas')

def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    tarea.delete()
    return redirect('lista_tareas')