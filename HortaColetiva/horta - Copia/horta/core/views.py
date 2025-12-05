from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def canteiros(request):
    return render(request, 'canteiros.html')

def producao(request):
    return render(request, 'producao.html')

def multiroes(request):
    return render(request, 'multiroes.html')

def relatorios(request):
    return render(request, 'relatorios.html')

