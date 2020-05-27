from django.urls import path
from . import views

urlpatterns = [
    path('colaborador/', views.colaborador_view, name = 'colaborador_view'),
    path('paciente/', views.paciente_view, name = 'paciente_view'),
	path('login/', views.login_view, name = 'user_login'),
    path('logout/', views.logout_view, name = 'user_logout'),
]
