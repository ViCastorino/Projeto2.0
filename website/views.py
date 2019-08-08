from django.shortcuts import render, redirect
from website.models import Instituicao, Paciente

# Create your views here.
def index(request):
    contexto= {}
    return render( request, 'index.html', contexto)

def login(request):
    contexto= {}
    return render( request, 'login.html', contexto)

def sobre(request):
    contexto= {}
    return render( request, 'sobre.html', contexto)

# função de cadastrar cliente
def cadastro(request):
     contexto= {}
     if request.method == 'POST':
          paciente = Paciente()
          paciente.nome = request.POST.get('nome')
          paciente.sobrenome = request.POST.get('sobrenome')
          paciente.genero = request.POST.get('genero')
          paciente.cpf = request.POST.get('cpf')
          paciente.telefone= request.POST.get('telefone')
          paciente.email = request.POST.get('email')
          paciente.senha = request.POST.get('senha')
          paciente.save()
          print('funcionou')
     return  render(request, 'cadastro.html', contexto)

#função de cadastrar as instituições

def cadastro_instituicao(request):
     contexto={ }
     if request.method == 'POST':
        instituicao = Instituicao()
        instituicao.nome_empresa = request.POST.get('nome_empresa')
        instituicao.email_comercial = request.POST.get('email_comercial')
        instituicao.cnpj = request.POST.get('cnpj') 
        instituicao.cep = request.POST.get('cep')
        instituicao.rua = request.POST.get('rua')
        instituicao.complemento = request.POST.get('complemento')
        instituicao.bairro = request.POST.get ('bairro')
        instituicao.municipio = request.POST.get ('municipio')
        instituicao.uf = request.POST.get ('uf')
        instituicao.senha = request.POST.get ('senha')
        instituicao.save()
        
     return render( request, 'index.html', contexto)

