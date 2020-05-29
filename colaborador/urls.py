from django.urls import path
from . import views

urlpatterns = [
    path('', views.colaborador_view, name = 'colaborador_view'),
    path('cadastro/', views.cadastro_colaborador_view, name = 'cadastro_colaborador_view'),
]
