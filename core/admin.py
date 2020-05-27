from django.contrib import admin

from .models import Usuario
from .models import Colaborador
from .models import Paciente


admin.site.register(Usuario)
admin.site.register(Colaborador)
admin.site.register(Paciente)
