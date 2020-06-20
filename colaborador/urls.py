from django.urls import path
from . import views
from core.carga import carga

urlpatterns = [
    path('', views.colaborador_view, name = 'colaborador_view'),
    path('cadastro/', views.cadastro_colaborador_view, name = 'cadastro_colaborador_view'),
    path('teste/', carga, name = 'cadastro_colaborador_carga'),
]
