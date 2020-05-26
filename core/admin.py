from django.contrib import admin

from .models import Usuario
from .models import Colaborador


admin.site.register(Usuario)
admin.site.register(Colaborador)
