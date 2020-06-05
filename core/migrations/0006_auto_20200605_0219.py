# Generated by Django 3.0.5 on 2020-06-05 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200605_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='idade',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='orientacao_sexual',
            field=models.CharField(choices=[('HOMO', 'Homossexual'), ('HETERO', 'Heterossexual'), ('BI', 'Bissexual'), ('INDEFINIDO', 'Prefiro não informar')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True),
        ),
    ]
