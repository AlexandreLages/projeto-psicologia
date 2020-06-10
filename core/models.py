from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    SEXO_CHOICES = {
        ("F", "Feminino"),
        ("M", "Masculino")
    }

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=255, null=False)
    telefone_celular = models.CharField(max_length=255, null=True, default='')
    telefone_fixo = models.CharField(max_length=255, null=True, default='')
    cpf = models.CharField(max_length=255, null=True, default='')
    rg = models.CharField(max_length=255, null=True, default='')
    email = models.CharField(max_length=255, null=True, default='')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True)

    class Meta:
        db_table = 'tbUsuario'


class Colaborador(Usuario):
    crp = models.CharField(max_length=50, null=False)
    perfil = models.TextField(default='')
    verificado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='imagens/', default='imagens/None/no-img.jpg')

    class Meta:
        db_table = 'tbColaborador'


class Paciente(Usuario):
    ORIENTACAO_CHOICES = {
        ("HETERO", "Heterossexual"),
        ("HOMO", "Homossexual"),
        ("BI", "Bissexual"),
        ("INDEFINIDO", "Prefiro não informar")
    }

    data_nascimento = models.DateField(null=True)
    orientacao_sexual = models.CharField(max_length=10, choices=ORIENTACAO_CHOICES, null=True)

    class Meta:
        db_table = 'tbPaciente'


class Administrador(Usuario):

    class Meta:
        db_table = 'tbAdministrador'


class Atendimento(models.Model):
    data_atendimento = models.DateField(null=False)
    colaborador = models.OneToOneField(Colaborador, on_delete=models.DO_NOTHING)
    paciente = models.OneToOneField(Paciente, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbAtendimento'
