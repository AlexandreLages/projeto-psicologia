from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from core.models import Usuario
from core.models import Colaborador


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['senha']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            usuario = Usuario.objects.get(user=user)
            if is_colaborador(usuario):
                return redirect('/colaborador/', {'message': 'Usuário logado com sucesso!'})
            else:
                return redirect('/paciente/', {'message': 'Usuário logado com sucesso!'})
        else:
            return redirect('/user/login/', {'message': 'Usuário/Senha inválidos!'})


def logout_view(request):
	logout(request)
	return redirect('/user/login/', {'message': 'Usuário logado com sucesso!'})


def is_colaborador(usuario):
    if Colaborador.objects.filter(usuario_ptr_id=usuario.id):
        return True
    else:
        return False