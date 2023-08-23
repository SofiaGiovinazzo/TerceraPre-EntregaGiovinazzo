from django.shortcuts import render
from AppFullSailing.forms import *
from AppFullSailing.models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio_admin(request):
    return render(request, 'inicio_admin.html')

@login_required
class ExamenList(ListView):
    model = Examen
    template_name = 'examen_list.html'
