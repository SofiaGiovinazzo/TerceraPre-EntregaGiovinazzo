from django.http import HttpResponse
from django.shortcuts import render
from AppFullSailing.models import Alumno, Profesor, Examen
from AppFullSailing.forms import AlumnosFormulario, ProfesoresFormulario, ExamenesFormulario


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def Alumnos(request):
    return render(request, 'Alumnos.html')

def Profesores(request):
    return render (request, 'Profesores.html')

def Examenes(request):
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

def profesoresFormulario(request):
    print("llegue1")
    if request.method == 'POST': 
        print("llegue2")

        miFormulario = ProfesoresFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            print("llegue3")
            
            profesores =Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            profesores.save()
            
            return render(request, 'inicio.html')
    else:
        print('llegue4')
        miFormulario = ProfesoresFormulario()
    
    return render(request, 'ProfesoresFormulario.html', {'miFormulario': miFormulario})

def examenesFormulario(request):
    print("llegue1")
    if request.method == 'POST': 
        print("llegue2")

        miFormulario = ExamenesFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            print("llegue3")
            
            examenes =Examen(embarcacion=informacion['embarcacion'], profe_examinador=informacion['profe_examinador'], fecha_examen=informacion['fecha_examen'])
            examenes.save()
            
            return render(request, 'inicio.html')
    else:
        print('llegue4')
        miFormulario = ExamenesFormulario()
    
    return render(request, 'ExamenesFormulario.html', {'miFormulario': miFormulario})



