from django.urls import path
from AppFullSailing import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('Alumnos', views.Alumnos, name= 'Alumnos'),
    path('Profesores', views.Profesores, name= 'Profesores'),
    path('Examen', views.Examenes, name= 'Examen'),
    #path('AlumnosFormulario', views.alumnosFormulario, name= 'AlumnosFormulario'),
    #path('ProfesoresFormulario', views.profesoresFormulario, name= 'ProfesoresFormulario'),
    #path('ExamenesFormulario', views.examenesFormulario, name= 'ExamenesFormulario'),
    path('controlFecha_examen', views.controlFecha_examen, name='ControlFecha_examen'),
    path('buscar/', views.buscar)

]
