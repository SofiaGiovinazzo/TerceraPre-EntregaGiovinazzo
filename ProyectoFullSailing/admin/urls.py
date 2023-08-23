from django.urls import path
from admin import views


urlpatterns = [
    path('', views.inicio_admin, name='Inicio_admin'),
    path('examen_list', views.ExamenList.as_view(), name= 'List'),

    
    

]