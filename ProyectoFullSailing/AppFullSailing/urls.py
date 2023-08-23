from django.urls import path
from AppFullSailing import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('Alumnos', views.Alumnos, name= 'Alumnos'),
    path('Profesores', views.Profesores, name= 'Profesores'),
    path('Examen', views.Examenes, name= 'Examen'),
    #path('AlumnosFormulario', views.alumnosFormulario, name= 'AlumnosFormulario'),
    #path('ProfesoresFormulario', views.profesoresFormulario, name= 'ProfesoresFormulario'),
    #path('ExamenesFormulario', views.examenesFormulario, name= 'ExamenesFormulario'),
    path('controlFecha_examen', views.controlFecha_examen, name='ControlFecha_examen'),
    path('buscar/', views.buscar),
    path('leerProfesores', views.leerProfesores, name = 'LeerProfesores'),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name='EliminarProfesor'),
    path('leerAlumnos', views.leerAlumnos, name = 'LeerAlumnos'),
    path('eliminarAlumno/<alumno_nombre>/', views.eliminarAlumno, name='EliminarAlumno'),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name='EditarProfesor'),
    path('editarAlumno/<alumno_nombre>/', views.editarAlumno, name='EditarAlumno'),
    #path(r'(?p<pk>\d+)$', views.ExamenDetalle.as_view(), name= 'Detail'),
    #path(r'^nuevo$', views.ExamenCreacion.as_view(), name= 'New'),
    #path(r'editar/(?P<pk>\d+)$', views.ExamenUpdate.as_view(), name= 'Edit'),
    #path(r'borrar/(?P<pk>\d+)$', views.ExamenDelete.as_view(), name= 'Delete'),
    path('examen_list', views.ExamenList.as_view(), name= 'List'),
    path('<int:pk>/', views.ExamenDetalle.as_view(), name='Detail'), 
    path('borrar/<int:pk>/', views.ExamenDelete.as_view(), name='Delete'),  
    path('editar/<int:pk>/', views.ExamenUpdate.as_view(), name='Edit'),  
    path('nuevo/', views.ExamenCreacion.as_view(), name='New'), 
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),



]


