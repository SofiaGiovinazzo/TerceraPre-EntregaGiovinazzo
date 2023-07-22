from django.http import HttpResponse
from django.shortcuts import render
from AppFullSailing.models import Alumno, Profesor, Examen
from AppFullSailing.forms import AlumnosFormulario, ProfesoresFormulario, ExamenesFormulario
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

#def Alumnos(request):
    return render(request, 'Alumnos.html')

#def Profesores(request):
    return render (request, 'Profesores.html')

#def Examenes(request):
    return render(request, 'Examen.html')

def Alumnos(request):
    if request.method == 'POST': 

        miFormulario = AlumnosFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            
            alumnos = Alumno(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], email=informacion['email'])
            alumnos.save()
            
            return render(request, 'inicio.html')
    else:
        miFormulario = AlumnosFormulario()
    
    return render(request, 'Alumnos.html', {'miFormulario': miFormulario})

def Profesores(request):
    if request.method == 'POST': 

        miFormulario = ProfesoresFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            
            profesores =Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            profesores.save()
            
            return render(request, 'inicio.html')
    else:
        miFormulario = ProfesoresFormulario()
    
    return render(request, 'Profesores.html', {'miFormulario': miFormulario})

def Examenes(request):
    if request.method == 'POST': 

        miFormulario = ExamenesFormulario(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            
            examenes =Examen(embarcacion=informacion['embarcacion'], profe_examinador=informacion['profe_examinador'], fecha_examen=informacion['fecha_examen'])
            examenes.save()
            
            return render(request, 'inicio.html')
    else:
        miFormulario = ExamenesFormulario()
    
    return render(request, 'Examenes.html', {'miFormulario': miFormulario})

def controlFecha_examen(request):
    return render(request,'controlFecha_examen.html' )

def buscar(request):
    if request.GET['fecha_examen']:

        #respuesta = f'esta es la fecha buscada: {request.GET["fecha_examen"]}'
        fecha_examen= request.GET['fecha_examen']
        examenes= Examen.objects.filter(fecha_examen__icontains=fecha_examen)

        return render(request, 'inicio.html', {'Examenes': examenes, 'fecha_examen': fecha_examen})
    
    else:
        respuesta = "No se encontraron los datos."

    #return HttpResponse(respuesta)
    return render(request, 'inicio.html', {'respuesta': respuesta})

