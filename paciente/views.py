from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
import requests, json

from core.models import Paciente
from core.utils.Cidade import Cidade
from core.utils.Estado import Estado


@login_required
def paciente_view(request):
    if request.method == 'GET':
        return render(request, 'paciente.html')


def get_cidades(request):
    id_estado = request.GET.get('id_estado')
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + id_estado + '/municipios'
    r = requests.get(url, params={'orderBy': 'nome'})
    cidades = json.loads(r.text)
    lista_cidades = []
    for cidade in cidades:
        lista_cidades.append(Cidade(cidade['id'], cidade['nome']))
    return render(request, 'cadastro_paciente.html', {'cidades': lista_cidades})


def cadastro_paciente_view(request):
    if request.method == 'GET':
        r = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados', params={'orderBy': 'nome'})
        estados = json.loads(r.text)
        lista_estados = []
        for estado in estados:
            lista_estados.append(Estado(estado['id'], estado['nome']))
        return render(request, 'cadastro_paciente.html', {'estados': lista_estados})
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
            return render('cadastro_paciente.html', {'message': 'Já existe uma pessoa com esse usuário!'})

        return redirect('/user/login/', {'message': 'Cadastro de paciente realizado com sucesso!'})

    return redirect('/user/login/')
