# Generated by Django 4.2.7 on 2023-11-16 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_sesion_options_remove_sala_sesion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='sala',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.sala'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='sesion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.sesion'),
        ),
        migrations.AlterField(
            model_name='sesion',
            name='horario',
            field=models.TimeField(),
        ),
    ]
