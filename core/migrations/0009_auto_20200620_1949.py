# Generated by Django 3.0.5 on 2020-06-20 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200613_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.CharField(max_length=5)),
                ('status', models.CharField(choices=[('ACEITO', 'Aceito'), ('REALIZADO', 'Realizado'), ('CANCELADO', 'Cancelado'), ('ANALISE', 'Em Análise')], max_length=50)),
                ('motivo', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('PSICOTERAPIA', 'Psicoterapia'), ('PLANTAO', 'Plantão')], max_length=50)),
            ],
            options={
                'db_table': 'tbAgendamento',
            },
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=255)),
                ('descricao', models.CharField(default='', max_length=255, null=True)),
                ('colaboradores', models.ManyToManyField(to='core.Colaborador')),
            ],
            options={
                'db_table': 'tbEspecialidadeColaborador',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[(4, 'Quarta-Feira'), (5, 'Quinta-Feira'), (3, 'Terça-Feira'), (7, 'Sábado'), (2, 'Segunda-Feira'), (1, 'Domingo'), (6, 'Sexta-Feira')], max_length=1)),
                ('hora', models.CharField(max_length=5)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='horarios', to='core.Colaborador')),
            ],
            options={
                'db_table': 'tbHorario',
            },
        ),
        migrations.AlterField(
            model_name='paciente',
            name='orientacao_sexual',
            field=models.CharField(choices=[('INDEFINIDO', 'Prefiro não informar'), ('HETERO', 'Heterossexual'), ('HOMO', 'Homossexual'), ('BI', 'Bissexual')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('O', 'Outro'), ('F', 'Feminino'), ('M', 'Masculino')], max_length=1, null=True),
        ),
        migrations.DeleteModel(
            name='Atendimento',
        ),
    ]