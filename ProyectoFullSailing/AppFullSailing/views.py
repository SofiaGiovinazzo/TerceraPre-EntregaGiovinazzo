from django.http import HttpResponse
from django.shortcuts import render
from AppFullSailing.models import Alumno, Profesor, Examen
from AppFullSailing.forms import AlumnosFormulario, ProfesoresFormulario, ExamenesFormulario, UserRegisterForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

#def Alumnos(request):
    return render(request, 'Alumnos.html')

#def Profesores(request):
    return render (request, 'Profesores.html')

#def Examenes(request):
    return render(request, 'Examen.html')

@login_required
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

@login_required
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

@login_required
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

@login_required
def controlFecha_examen(request):
    return render(request,'controlFecha_examen.html' )

def buscar(request):
    if request.GET['fecha_examen']:

        #respuesta = f'Esta es la fecha buscada: {request.GET["fecha_examen"]}'
        fecha_examen= request.GET['fecha_examen']
        examenes= Examen.objects.filter(fecha_examen__icontains=fecha_examen)

        return render(request, 'inicio.html', {'Examenes': examenes, 'fecha_examen': fecha_examen})
    
    else:
        respuesta = "No se encontraron los datos."

    #return HttpResponse(respuesta)
    return render(request, 'inicio.html', {'respuesta': respuesta})

def leerProfesores(request):
    profesores = Profesor.objects.all() #trae todos los profesores
    contexto = {'profesores':profesores}

    return render(request, 'leerProfesores.html', contexto)

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {'profesores':profesores}

    return render(request, 'leerProfesores.html', contexto)

def leerAlumnos(request):
    alumnos = Alumno.objects.all()
    contexto = {'alumnos':alumnos}

    return render(request, 'leerAlumnos.html', contexto) 

def eliminarAlumno(request, alumno_nombre):
    alumno = Alumno.objects.get(nombre=alumno_nombre) 
    alumno.delete()

    alumnos = Alumno.objects.all()
    contexto = {'alumnos':alumnos}

    return render(request, 'leerAlumnos.html', contexto) 

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == 'POST':
        miFormulario = ProfesoresFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']

            profesor.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = ProfesoresFormulario(initial={'nombre': profesor.nombre, 
                                                     'apellido': profesor.apellido, 
                                                     'email': profesor.email})
    return render(request, 'editarProfesor.html', {'miFormulario': miFormulario, 'profesor_nombre': profesor_nombre})


def editarAlumno(request, alumno_nombre):
    alumno = Alumno.objects.get(nombre=alumno_nombre)

    if request.method == 'POST':
        miFormulario = AlumnosFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            alumno.nombre = informacion['nombre']
            alumno.apellido = informacion['apellido']
            alumno.edad = informacion['edad']
            alumno.email = informacion['email']

            alumno.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = AlumnosFormulario(initial={'nombre': alumno.nombre, 
                                                  'apellido': alumno.apellido, 
                                                  'edad': alumno.edad, 
                                                  'email': alumno.email})
    return render(request, 'editarAlumno.html', {'miFormulario': miFormulario, 'alumno_nombre': alumno_nombre})
    
class ExamenList(ListView):
    model = Examen
    template_name = 'examen_list.html'

class ExamenDetalle(DetailView):
    model = Examen
    template_name = 'examen_detalle.html'

class ExamenCreacion(CreateView):
    model = Examen
    success_url = 'AppFullSailing/examen/list'
    fields = ['embarcacion', 'profe_examinador', 'fecha_examen']

class ExamenUpdate(UpdateView):
    model = Examen
    success_url = 'AppFullSailing/examen/list'
    fields = ['embarcacion', 'profe_examinador', 'fecha_examen']

class ExamenDelete(DeleteView):
    model = Examen
    success_url = 'AppFullSailing/examen/list'

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contras)

            if user is not None:
                login(request, user)
                return render(request, 'inicio.html', {'mensaje': f"Bienvenido {usuario}"})
            
            else:
                return render(request, 'inicio.html', {'mensaje': 'Error, usuario incorrecto'})
        else:
            return render(request, 'inicio.html', {'mensaje': 'Error, formulario incorrecto'} )
        
    form = AuthenticationForm()

    return render(request, 'login.html', {'form':form})


def register(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, 'inicio.html', {'mensaje': 'Usuario creado correctamente'})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)
       
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
           
            usuario.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, 'editarPerfil.html', {'miFormulario': miFormulario, 'usuario':usuario})
