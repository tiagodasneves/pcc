# Generated by Django 4.2 on 2023-04-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('rua', models.CharField(max_length=255, null=True)),
                ('bairro', models.CharField(max_length=255, null=True)),
                ('cidade', models.CharField(max_length=255, null=True)),
                ('estado', models.CharField(max_length=2, null=True)),
                ('regiao', models.CharField(choices=[('NO', 'Norte'), ('NE', 'Nordeste'), ('SE', 'Sudeste'), ('CO', 'Centro-Oeste'), ('SU', 'Sul')], default='NO', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('rua', models.CharField(max_length=255, null=True)),
                ('bairro', models.CharField(max_length=255, null=True)),
                ('cidade', models.CharField(max_length=255, null=True)),
                ('estado', models.CharField(max_length=2, null=True)),
                ('regiao', models.CharField(choices=[('NO', 'Norte'), ('NE', 'Nordeste'), ('SE', 'Sudeste'), ('CO', 'Centro-Oeste'), ('SU', 'Sul')], default='NO', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
