# Generated by Django 2.2.4 on 2019-08-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190808_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='bairro',
            field=models.CharField(default='Bela vista', max_length=255, verbose_name='bairro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='cep',
            field=models.CharField(default='34243242', max_length=255, verbose_name='CEP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='cidade',
            field=models.CharField(default='sim', max_length=255, verbose_name='Cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='complemento',
            field=models.CharField(default='fgg', max_length=255, verbose_name='complemento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='data_nasc',
            field=models.CharField(default='meudeus', max_length=255, verbose_name='Data de Nascimento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='rua',
            field=models.CharField(default='rua', max_length=255, verbose_name='Rua'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='uf',
            field=models.CharField(default='BA', max_length=255, verbose_name='Uf'),
            preserve_default=False,
        ),
    ]