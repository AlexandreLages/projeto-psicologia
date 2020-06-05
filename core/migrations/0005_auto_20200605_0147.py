# Generated by Django 3.0.5 on 2020-06-05 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_colaborador_verificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='idade',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='orientacao_sexual',
            field=models.CharField(choices=[('BI', 'Bissexual'), ('HOMO', 'Homossexual'), ('HETERO', 'Heterossexual'), ('INDEFINIDO', 'Prefiro não informar')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1, null=True),
        ),
    ]
