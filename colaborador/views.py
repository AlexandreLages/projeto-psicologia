import urllib
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.conf import settings

from core.models import Colaborador


@login_required
def colaborador_view(request):
    if request.method == 'GET':
        return render(request, 'colaborador.html')


def cadastro_colaborador_view(request):
	if request.method == 'GET':
		return render(request, 'cadastro_colaborador.html')
	elif request.method == 'POST':

		''' Begin reCAPTCHA validation '''
		recaptcha_response = request.POST.get('g-recaptcha-response')
		url = 'https://www.google.com/recaptcha/api/siteverify'
		values = {
			'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
			'response': recaptcha_response
		}
		data = urllib.parse.urlencode(values).encode('utf-8')
		req = urllib.request.Request(url)
		req.add_header("Content-type", "application/x-www-form-urlencoded")
		req.add_header("User-agent", "reCAPTCHA Python")
		response = urllib.request.urlopen(req, data)
		result = json.load(response)
		''' End reCAPTCHA validation '''

		if result['success']:
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
		else:
			return render(request, 'cadastro_colaborador.html', {'message': 'Erro na validação do reCAPTCHA! Tente novamente.'})