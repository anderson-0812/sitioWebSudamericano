# Generated by Django 2.1.5 on 2019-01-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExAlumnos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonios',
            name='fecha_hora',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Time'),
        ),
    ]
