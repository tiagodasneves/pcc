# Generated by Django 4.2.3 on 2023-07-11 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peruca',
            name='foto',
            field=models.ImageField(null=True, upload_to='imagens/perucas'),
        ),
        migrations.AddField(
            model_name='solicitacaoperuca',
            name='comprovante',
            field=models.ImageField(null=True, upload_to='imagens/comprovantes'),
        ),
        migrations.AlterField(
            model_name='peruca',
            name='cor',
            field=models.CharField(choices=[('loiro', 'Peruca de cabelo loiro'), ('ruivo', 'Peruca de cabelo ruivo'), ('preto', 'Peruca de cabelo preto'), ('castanho', 'Peruca de cabelo castanho'), ('grisalho', 'Peruca de cabelo grisalho')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='peruca',
            name='selecionada',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='peruca',
            name='tamanho',
            field=models.CharField(choices=[('curto', 'Peruca de tamanho curto'), ('medio', 'Peruca de tamanho médio'), ('longo', 'Peruca de tamanho longo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='peruca',
            name='tipo',
            field=models.CharField(choices=[('liso', 'Peruca de cabelo liso'), ('ondulado', 'Peruca de cabelo ondulado'), ('cacheado', 'Peruca de cabelo cacheado'), ('crespo', 'Peruca de cabelo crespo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='solicitacaoperuca',
            name='questao1',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='solicitacaoperuca',
            name='questao2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='solicitacaoperuca',
            name='questao3',
            field=models.TextField(null=True),
        ),
    ]