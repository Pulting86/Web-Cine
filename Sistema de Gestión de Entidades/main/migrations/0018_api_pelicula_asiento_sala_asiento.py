# Generated by Django 4.2.7 on 2023-11-19 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0017_alter_pelicula_options_remove_sesion_pelicula_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='API_Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('photo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservado', models.BooleanField()),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sala',
            name='asiento',
            field=models.ManyToManyField(to='main.asiento'),
        ),
    ]
