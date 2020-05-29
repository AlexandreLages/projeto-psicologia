# Generated by Django 3.0.5 on 2020-05-29 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200526_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Usuario')),
            ],
            options={
                'db_table': 'tbAdministrador',
            },
            bases=('core.usuario',),
        ),
    ]