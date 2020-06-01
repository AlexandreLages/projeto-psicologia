from django.urls import path
from . import views

urlpatterns = [
    path('', views.paciente_view, name = 'paciente_view'),
    path('cadastro/', views.cadastro_paciente_view, name = 'cadastro_paciente_view'),
]
