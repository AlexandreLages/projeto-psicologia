from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def paciente_view(request):
    if request.method == 'GET':
        return render(request, 'paciente.html')