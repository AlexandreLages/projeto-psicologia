from django.urls import path
from . import views

urlpatterns = [
    path('', views.colaborador_view, name = 'colaborador_view'),
]
