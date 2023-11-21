# Generated by Django 4.2.7 on 2023-11-16 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_perfil_delete_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sesion',
            options={'ordering': ['horario']},
        ),
        migrations.RemoveField(
            model_name='sala',
            name='sesion',
        ),
        migrations.RemoveField(
            model_name='sesion',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='sesion',
            name='pelicula',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='sala',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.sala'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='sesion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.sesion'),
        ),
        migrations.AddField(
            model_name='sesion',
            name='horario',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
