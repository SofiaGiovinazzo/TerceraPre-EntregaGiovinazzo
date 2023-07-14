from django.http import HttpResponse
from django.shortcuts import render
from AppFullSailing.forms import alumnosFormulario


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
    if request.method == 'POST':
        miFormulario = alumnosFormulario(request.post) 
        print(miFormulario)

        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            
            Alumnos = Alumnos(nombre=informacion['Nombre'], apellido=informacion['Apellido'], edad=informacion['Edad'], email=informacion['Email'])
            Alumnos.save()
            
            return render(request, 'inicio.html')
   # else:
    #    miFormulario = AlumnosFormulario()
    
    return render(request, 'AlumnosFormulario.html', {'miFormulario': miFormulario})


