# Generated by Django 3.0.5 on 2020-05-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_administrador'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='verificado',
            field=models.BooleanField(default=False),
        ),
    ]
