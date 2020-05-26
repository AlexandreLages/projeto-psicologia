from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from core.models import Usuario


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
            return redirect('/user/', {'message': 'Usuário logado com sucesso!'})
        else:
            return render(request, 'login.html', {'message': 'Usuário/Senha inválidos!'})


def logout_view(request):
	logout(request)
	return redirect('/user/login/', {'message': 'Usuário logado com sucesso!'})


@login_required
def user_view(request):
    if request.method == 'GET':
        return render(request, 'user.html')
