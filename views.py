from django.shortcuts import render
from django.http import HttpResponse
from .models import matricula  # Modelo com os dados que você quer exibir nos cards
# from .models import prontuarios

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Create your views here.
def planejamento(request):
    matriculas = matricula.objects.all()  # Query para buscar todos os registros
    print(matriculas)
    return render(request, 'planejamento.html', {'matriculas': matriculas})

# Create your views here.
def prontuarios_view(request):
    
    if request.method == "GET":
        return render(request, 'prontuarios.html')
    if request.method == "POST":
        Nome = request.POST.get('nome')

        return HttpResponse("Nome Salvo com sucesso!! -->  "+ Nome)