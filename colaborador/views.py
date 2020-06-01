from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render

from core.models import Colaborador


@login_required
def colaborador_view(request):
    if request.method == 'GET':
        return render(request, 'colaborador.html')


def cadastro_colaborador_view(request):
	if request.method == 'GET':
		return render(request, 'cadastro_colaborador.html')
	elif request.method == 'POST':
		usuario = request.POST['usuario']
		senha = request.POST['senha']
		confirma_senha = request.POST['confirmarSenha']
		email = request.POST['email']
		nome = request.POST['nome']
		telefone = request.POST['telefone']
		celular = request.POST['celular']
		cpf = request.POST['cpf']
		rg = request.POST['rg']
		crp = request.POST['crp']
		perfil = request.POST['perfil']
		colaborador = None

		user = User.objects.filter(username=usuario)

		if not user:
			user = User.objects.create_user(usuario, email, senha)
			user.save()

			colaborador = Colaborador(
				nome=nome,
				telefone_celular=celular,
				telefone_fixo=telefone,
				cpf=cpf,
				rg=rg, email=email,
				crp=crp, perfil=perfil
			)

			user = User.objects.get(username=usuario)
			colaborador.user = user
			colaborador.save()
		else:
			return render(request, 'cadastro_colaborador.html', {'message': 'Já existe uma pessoa com esse usuário!'})

		return redirect('/user/login/', {'message': 'Cadastro de colaborador realizado com sucesso!'})

	return redirect('/user/login/')