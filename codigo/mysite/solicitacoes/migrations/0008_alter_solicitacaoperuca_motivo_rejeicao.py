# Generated by Django 4.2.3 on 2023-08-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes', '0007_remove_solicitacaoperuca_comprovante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacaoperuca',
            name='motivo_rejeicao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
