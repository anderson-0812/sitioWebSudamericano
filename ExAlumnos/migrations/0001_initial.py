# Generated by Django 2.1.5 on 2019-01-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exalumnos',
            fields=[
                ('id_exalumno', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('M', 'Mujer'), ('H', 'Hombre')], default='H', max_length=1)),
            ],
            options={
                'verbose_name': 'Exalumnos',
                'verbose_name_plural': 'Exalumnos',
                'db_table': 'exalumnos',
            },
        ),
    ]