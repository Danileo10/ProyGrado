# Generated by Django 4.1.7 on 2023-05-16 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0002_alter_mascota_id_clienteid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hora', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('cupo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('id_bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.bloque')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.cliente')),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.servicio')),
            ],
        ),
    ]
