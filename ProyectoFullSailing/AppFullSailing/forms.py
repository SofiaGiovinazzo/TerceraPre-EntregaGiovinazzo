from django import forms

class AlumnosFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    email = forms.EmailField()

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class ExamenesFormulario(forms.Form):
    embarcacion = forms.CharField(max_length=10)
    profe_examinador = forms.CharField(max_length=30)
    fecha_examen = forms.DateField()
    
