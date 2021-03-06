# Generated by Django 3.1.3 on 2020-11-09 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('Estado', models.CharField(max_length=20)),
                ('Coordenadas', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Chip',
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=102)),
                ('apellido', models.CharField(max_length=102)),
                ('documento', models.CharField(max_length=102, unique=True)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Departamento',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=100)),
                ('id_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlGanado.departamento')),
            ],
            options={
                'verbose_name_plural': 'Municipio',
            },
        ),
        migrations.CreateModel(
            name='Veredas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vereda', models.CharField(max_length=102)),
                ('indicaciones', models.TextField()),
                ('id_municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlGanado.municipio')),
            ],
            options={
                'verbose_name_plural': 'Veredas',
            },
        ),
        migrations.CreateModel(
            name='HistorialChip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=20)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('id_chip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlGanado.chip')),
            ],
            options={
                'verbose_name_plural': 'Historial Chip',
            },
        ),
        migrations.CreateModel(
            name='Fincas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finca', models.CharField(max_length=102)),
                ('indicaciones', models.TextField()),
                ('id_vereda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlGanado.veredas')),
            ],
            options={
                'verbose_name_plural': 'Fincas',
            },
        ),
        migrations.CreateModel(
            name='Bovinos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Raza', models.CharField(max_length=100)),
                ('Genero', models.CharField(max_length=50)),
                ('Color', models.CharField(max_length=50)),
                ('Sexo', models.CharField(max_length=50)),
                ('chip', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ControlGanado.chip')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlGanado.clientes')),
                ('id_finca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ControlGanado.fincas')),
            ],
            options={
                'verbose_name_plural': 'Bovinos',
            },
        ),
    ]
