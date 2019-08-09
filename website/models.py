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

    data_nasc = models.CharField(
        max_length= 255,
        verbose_name= 'Data de Nascimento'
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

    cep = models.CharField(
        max_length= 255,
        verbose_name= 'CEP'
    )
    rua = models.CharField(
        max_length= 255,
        verbose_name= 'Rua'
    )

    complemento= models.CharField(
        max_length= 255,
        verbose_name= 'complemento'
    )

    bairro = models.CharField(
        max_length= 255,
        verbose_name= 'bairro'
    )
    cidade= models.CharField(
        max_length= 255,
        verbose_name= 'Cidade'
    )
    
    uf = models.CharField(
        max_length= 255,
        verbose_name= 'Uf'
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
        return self.nome + str(' ') + self.sobrenome
        


class Instituicao(models.Model):

    nome_empresa = models.CharField(
        max_length = 255,
        verbose_name='Nome',        
        null= True,
        blank = True
    )

    cnpj = models.CharField(
        max_length = 255,
        verbose_name = 'CNPJ',
        null= True,
        blank = True
    )

    telefone_comercial = models.CharField(
        max_length= 255,
        verbose_name='Telefone Comercial',
    )
    
    cep = models.CharField(
        max_length=255,
        verbose_name='Endereço'
    )

    rua = models.CharField(
        max_length=255,
        verbose_name='Endereço'
    )
    
    complemento = models.CharField(
        max_length=255,
        verbose_name='Complemento'
    )
        
    bairro = models.CharField(
        max_length= 255,
        verbose_name='Bairro'
    )

    municipio = models.CharField(
        max_length=255,
        verbose_name='Município'
    )
    
    uf = models.CharField(
        max_length=255,
        verbose_name='UF'
    )

    email_comercial = models.EmailField(
        max_length=255,
        verbose_name='E-mail Comercial'
    )

    senha = models.CharField(
        max_length = 255,
        verbose_name='Senha'
    )

    def __str__(self):
        return self.nome_empresa + str(' ') + self.cnpj

    
