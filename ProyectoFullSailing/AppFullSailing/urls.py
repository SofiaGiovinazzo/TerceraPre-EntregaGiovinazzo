from django.urls import path
from AppFullSailing import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('Alumnos', views.Alumnos, name= 'Alumnos'),
    path('Profesores', views.Profesores, name= 'Profesores'),
    path('Examen', views.Examen, name= 'Examen'),
    path('AlumnosFormulario', views.alumnosFormulario, name= 'AlumnosFormulario'),

    
]