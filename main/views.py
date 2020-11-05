from django.shortcuts import render
from main.models import Automovel

# Create your views here.
# A partir desse ponto vamos criar funções responsáveis por coordernar
# a apresentação de views e templates do sistema web.
def index(response):

    context = {}
    automoveis = Automovel.objects.filter(quantidade_estoque__gt = 0)
    context['automoveis'] = automoveis
    return render(response, 'main/index.html', context)