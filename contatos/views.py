from django.shortcuts import render

def contatos(request):
    return render(request, 'contatos/contatos.html')
