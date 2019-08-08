from django.db import models

# Create your models here.

class Paciente(models.Model):
    
    GENEROS =(
        ('F', 'Feminino'),
        ('M', 'Masculino'),
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

    email = models.EmailField(
        max_length= 255,
        verbose_name= 'Email'
    )

    senha = models.CharField(
        max_length = 255,
        verbose_name='Senha'
    )

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
        max_length=100,
        verbose_name='UF'
    )

    senha = models.CharField(
        max_length = 8,
        verbose_name='Senha'
    )

    def __str__(self):
        return self.nome_empresa + ' ' + self.cnpj

    
