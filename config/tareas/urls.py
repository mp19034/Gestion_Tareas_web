from django.urls import path
from . import views

#cree este archivo.py llamado urls donde estaran los endpoint para redirigir las paginas
#ojo siempre revisar si esta agregado en config/urls.py el path de nuestros urls de tareas: path('', include('tareas.urls')),
urlpatterns = [
    #base adonde estara
    path('', views.lista_tareas, name='lista_tareas'),
    #el link para agregar las tareas
    path('agregar/', views.agregar_tarea, name='agregar_tarea'),
    #link de accion 
    path('completar/<int:tarea_id>/', views.marcar_completada, name='marcar_completada'),
    #link de accion delete
    path('eliminar/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea'),
]
