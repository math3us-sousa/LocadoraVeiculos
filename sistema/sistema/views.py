from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import redirect

class Login(View):
    def get(self, request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)
    
    def post(self, request):
        nome_usuario = request.POST.get('username')
        senha = request.POST.get('password')

        usuario = authenticate(request, username=nome_usuario, password=senha)

        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                return redirect('listar_veiculos')
            else:
                contexto = {'erro': 'Email ou senha inválidos.'}
                return render(request, 'autenticacao.html', contexto)
        else:
            contexto = {'erro': 'Email ou senha inválidos.'}
            return render(request, 'autenticacao.html', contexto)
