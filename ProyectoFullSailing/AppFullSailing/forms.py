from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class AvatarFormulario(forms.Form):
    avatar = forms.ImageField(label='Cargar Avatar', required=False)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modifical Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    avatar = forms.ImageField(label='Avatar', required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name', 'avatar']
        help_texts = {k:"" for k in fields}


