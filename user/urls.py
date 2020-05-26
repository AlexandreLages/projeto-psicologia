from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_view, name = 'user_view'),
	path('login/', views.login_view, name = 'user_login'),
    path('logout/', views.logout_view, name = 'user_logout'),
]
