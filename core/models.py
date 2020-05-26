from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'tbUsuario'


class Colaborador(Usuario):
    crp = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'tbColaborador'
