from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from core.models import Paciente


@login_required
def paciente_view(request):
    if request.method == 'GET':
        return render(request, 'paciente.html')


def cadastro_paciente_view(request):
	if request.method == 'GET':
		return render(request, 'cadastro_paciente.html')
	elif request.method == 'POST':
		usuario = request.POST['usuario']
		senha = request.POST['senha']
		confirma_senha = request.POST['confirmarSenha']
		email = request.POST['email']
		nome = request.POST['nome']
		telefone = request.POST['telefone']
		celular = request.POST['celular']
		cpf = request.POST['cpf']
		sexo = request.POST['sexo']
		orientacao_sexual = request.POST['orientacao']
		paciente = None

		user = User.objects.filter(username=usuario)

		if not user:
			user = User.objects.create_user(usuario, email, senha)
			user.save()

			paciente = Paciente(
				nome=nome,
				telefone_celular=celular,
				telefone_fixo=telefone,
				cpf=cpf,
				email=email,
				sexo=sexo,
				orientacao_sexual=orientacao_sexual
			)

			user = User.objects.get(username=usuario)
			paciente.user = user
			paciente.save()
		else:
			return render(request, 'cadastro_paciente.html', {'message': 'Já existe uma pessoa com esse usuário!'})

		return redirect('/user/login/', {'message': 'Cadastro de paciente realizado com sucesso!'})

	return redirect('/user/login/')