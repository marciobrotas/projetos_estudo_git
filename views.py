from django.shortcuts import render
from django.http import HttpResponse
from .models import prontuarios


# Create your views here.
def home(request):
    return render(request, 'home.html')

# Create your views here.
def prontuarios_view(request):
    
    if request.method == "GET":
        return render(request, 'prontuarios.html')
    if request.method == "POST":
        Nome = request.POST.get('nome')

        prontuario = prontuarios(
            nome = Nome
        )
        
        prontuario.save()

        return HttpResponse("Nome Salvo com sucesso!! -->  "+ Nome)