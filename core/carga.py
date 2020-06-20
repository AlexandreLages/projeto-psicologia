from .models import Especialidade
from .models import Horario
from .models import Agendamento
from .models import Colaborador
from .models import Paciente


def carga(request):
	colaborador = Colaborador.objects.filter()[0]
	paciente = Paciente.objects.filter()[0]

	especialidade = Especialidade(nome='Ansiedade', descricao='Trantorno de Ansiedade')
	especialidade.save()

	horario = Horario(dia=1, hora='10:00', colaborador=colaborador)
	horario.save()

	especialidade.colaboradores.add(colaborador)

	angedamento = Agendamento(data='2020-06-19', horario='10:00', status='ANALISE', motivo='Ansiedade', tipo='PLANTAO', colaborador=colaborador, paciente=paciente)
	angedamento.save()

	print(colaborador.nome)
	print(paciente.nome)

	return None