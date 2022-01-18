from django.shortcuts import render
from .models import Contato


def contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/contatos.html', {
        'contatos': contatos,
    })
