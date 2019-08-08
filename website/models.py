from django.db import models

# Create your models here.

class Paciente(models.Model):
    
    GENEROS =(
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('NB',  'Não Binário')
        ('T',  'Trans')
        ('O',  'Outros')
    )

    nome = models.CharField(
        max_length = 255,
        verbose_name= 'Nome'
    )

    sobrenome = models.CharField(
        max_length = 255,
        verbose_name= 'Sobrenome'
    )

    genero = models.CharField(
        max_length = 255,
        verbose_name= 'Gênero',
        choices=GENEROS
    )

    cpf= models.CharField(
        max_length = 255,
        verbose_name= 'CPF',
        null= False,
        blank = False
    )

    telefone = models.CharField(
        max_length= 255,
        verbose_name= 'Telefone Fixo'
    )

    cep = models.Charfield(
        max_length=255,
        verbose_name='CEP'
    )

    
    rua = models.Charfield(
        max_length=255,
        verbose_name='rua'
    )

    
    complemento = models.Charfield(
        max_length=255,
        verbose_name='complemento'
    )

    
    bairro = models.Charfield(
        max_length=255,
        verbose_name='bairro'
    )

    
    cidade = models.Charfield(
        max_length=255,
        verbose_name='cidade'
    )

    
    uf = models.Charfield(
        max_length=2,
        verbose_name='UF'
    )

    email = models.EmailField(
        max_length= 255,
        verbose_name= 'Email'
    )

    senha = models.CharField(
        max_length = 255,
        verbose_name='Senha'
    )

    data_de_criacao = models.DateTimeField( auto_now_add = True  ) 

    ativo = models.BooleanField( default = True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class Instituicao(models.Model):

    nome_empresa = models.CharField(
        max_length = 255,
        verbose_name='Nome',        
        null= True,
        blank = True
    )

    cnpj = models.CharField(
        max_length = 255,
        verbose_name = 'CNPJ'
    )
    
    email_comercial = models.EmailField(
        max_length=255,
        verbose_name='E-mail Comercial'
    )

    cep = models.CharField(
        max_length=9,
        verbose_name='Endereço'
    )
    cnpj = models.CharField(
        max_length=9,
        verbose_name='cnpj',
        null= True,
        blank = True
    )
    rua = models.CharField(
        max_length=100,
        verbose_name='Endereço'
    )
    
    complemento = models.CharField(
        max_length=6,
        verbose_name='Complemento'
    )
        
    bairro = models.CharField(
        max_length=100,
        verbose_name='Bairro'
    )

    municipio = models.CharField(
        max_length=50,
        verbose_name='Município'
    )
    
    uf = models.CharField(
        max_length=2,
        verbose_name='UF'
    )

    senha = models.CharField(
        max_length = 8,
        verbose_name='Senha'
    )

    data_de_criacao = models.DateTimeField( auto_now_add = True  ) 

    ativo = models.BooleanField( default = True)

    def __str__(self):
        return self.nome_empresa + ' ' + self.cnpj

    
