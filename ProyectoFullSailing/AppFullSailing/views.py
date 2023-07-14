from django.http import HttpResponse
from django.shortcuts import render
from AppFullSailing.models import Alumno
from AppFullSailing.forms import AlumnosFormulario


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def Alumnos(request):
    return render(request, 'Alumnos.html')

def Embarcacion(request):
    return render(request,'Embarcacion.html')

def Profesores(request):
    return render (request, 'Profesores.html')

def Examen(request):
    return render(request, 'Examen.html')

def alumnosFormulario(request):
    print("llegue1")
    if request.method == 'POST': 
        print("llegue2")

        miFormulario = AlumnosFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            print("llegue3")
            
            alumnos = Alumno(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], email=informacion['email'])
            alumnos.save()
            
            return render(request, 'inicio.html')
    else:
        print('llegue4')
        miFormulario = AlumnosFormulario()
    
    return render(request, 'AlumnosFormulario.html', {'miFormulario': miFormulario})


