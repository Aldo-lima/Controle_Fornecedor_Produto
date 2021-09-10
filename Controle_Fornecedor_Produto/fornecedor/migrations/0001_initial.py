# Generated by Django 3.2.7 on 2021-09-10 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=100, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Fantasia')),
                ('nome_r', models.CharField(max_length=100, verbose_name='Nome Razão Social')),
                ('CNPJ', models.CharField(max_length=100, verbose_name='cnpj')),
                ('escricao_estadual', models.CharField(max_length=100, verbose_name='Escrição Estadual')),
                ('rua', models.CharField(max_length=200, verbose_name='Rua')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('numero', models.IntegerField(verbose_name='Numéro')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('proximidade', models.CharField(max_length=30)),
                ('complemento', models.CharField(max_length=10, verbose_name='Complemento')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedor.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_contato', models.CharField(max_length=100, verbose_name='Nome')),
                ('cargo', models.CharField(max_length=10, verbose_name='Cargo')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('tipo_telefone', models.CharField(choices=[('pessoal', 'Pessoal'), ('comercial', 'Comercial')], max_length=11)),
                ('Email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('tipo_email', models.CharField(choices=[('pessoal', 'Pessoal'), ('comercial', 'Comercial')], max_length=11)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedor.fornecedor')),
            ],
        ),
    ]