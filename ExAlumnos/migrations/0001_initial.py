# Generated by Django 2.1.5 on 2019-01-16 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exalumnos',
            fields=[
                ('id_exalumno', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Exalumnos',
                'verbose_name_plural': 'Exalumnos',
                'db_table': 'exalumnos',
            },
        ),
        migrations.CreateModel(
            name='Testimonios',
            fields=[
                ('id_testimonio', models.AutoField(primary_key=True, serialize=False)),
                ('testimonio', models.TextField()),
                ('video', models.CharField(max_length=255)),
                ('id_exalumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExAlumnos.Exalumnos')),
            ],
            options={
                'verbose_name': 'Testimonio',
                'verbose_name_plural': 'testimonios',
                'db_table': 'testimonios',
            },
        ),
    ]
