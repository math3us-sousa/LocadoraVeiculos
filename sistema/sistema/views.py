from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import redirect

class Login(View):
    def get(self, request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)
    
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = authenticate(request, username=email, password=senha)

        if usuario is not None:
            if usuario.is_active:
                login(request, usuario)
                return redirect('home')
            else:
                contexto = {'erro': 'Email ou senha inválidos.'}
                return render(request, 'autenticacao.html', contexto)
        else:
            contexto = {'erro': 'Email ou senha inválidos.'}
            return render(request, 'autenticacao.html', contexto)
