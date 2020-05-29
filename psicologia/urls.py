from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('paciente/', include('paciente.urls')),
    path('colaborador/', include('colaborador.urls')),
]
