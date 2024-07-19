from django.shortcuts import render
from datetime import datetime

def index(request):
    lista_usuarios = [
        {"nome": "Ademacir Filho", "idade": 17},
        {"nome": "Lionel Messi", "idade": 37},
        {"nome": "Wiu", "idade": 25},
        {"nome": "Travis Scott", "idade": 29},
    ]
    
    context = {
        "usuarios": lista_usuarios,
    }
    return render(request, "index.html", context)