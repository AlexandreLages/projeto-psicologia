# Generated by Django 3.0.5 on 2020-06-13 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200610_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='orientacao_sexual',
            field=models.CharField(choices=[('BI', 'Bissexual'), ('HOMO', 'Homossexual'), ('HETERO', 'Heterossexual'), ('INDEFINIDO', 'Prefiro não informar')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')], max_length=1, null=True),
        ),
    ]
