# Generated by Django 3.2.2 on 2021-05-15 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('gestio_professor', 'Pot mantenir formulari i assignar projecte'),),
            },
        ),
        migrations.CreateModel(
            name='Seminari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('places', models.PositiveSmallIntegerField()),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='batxillerat_projecte.departament')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantajament', models.TextField()),
                ('assignat', models.BooleanField(default=False)),
                ('seminari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='batxillerat_projecte.seminari')),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('enviar_solicitud', 'Pot enviar Solicitud'),),
            },
        ),
    ]
