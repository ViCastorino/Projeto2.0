from django.shortcuts import render, redirect
from  website.models import Paciente, Instituicao

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

          # checar se o email já está cadastrado
          email_digitado = request.POST.get('email')
          em_uso = Paciente.objects.filter(email = email_digitado).first()
          print('ta funcionando')

          if(em_uso is None):
               print('ta jkjjh')
               paciente.nome = request.POST.get('nome')
               paciente.sobrenome = request.POST.get('sobrenome')
               paciente.data_nasc = request.POST.get('data_nasc')
               paciente.genero = request.POST.get('genero')
               paciente.cpf = request.POST.get('cpf')
               paciente.telefone= request.POST.get('telefone')
               paciente.cep = request.POST.get('cep')
               paciente.rua = request.POST.get('rua')
               paciente.complemento = request.POST.get('complemento')
               paciente.bairro = request.POST.get('bairro')
               paciente.cidade = request.POST.get('cidade')
               paciente.uf = request.POST.get('uf')
               paciente.email = request.POST.get('email')
               paciente.senha = request.POST.get('senha')
               print(paciente)
               paciente.save()
               print(paciente)
               contexto= {'msg':f'Boas vindas, {paciente.nome}! Aproveite o site :) '}
               print(f'{paciente.nome} foi cadastrado')
               return  render(request, 'login.html', contexto)
          # return render(request, 'cadastro.html', contexto)
          else:
               contexto = {'msg':f'Parece que este email já está sendo utilizado :('}
               print('error')
               return render(request, 'cadastro.html', contexto)
     return render(request, 'cadastro.html', {})

#função de cadastrar as instituições
def cadastro_instituicao(request):
     contexto={ }
     if request.method == 'POST':
        
        email_digitado_inst = request.POST.get('email')
        em_uso_inst = Pessoa.objects.filter(email = email_digitado_inst).first()
          
        if(em_uso is None):
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
     
        else:
          contexto= {'msg':f'Ooops, parece que já cadastraram esse email'}
          return  render(request, 'login.html', contexto)
        
     return render( request, 'index.html', contexto)

