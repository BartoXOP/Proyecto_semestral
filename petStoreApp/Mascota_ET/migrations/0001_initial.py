# Generated by Django 3.2.14 on 2022-07-10 01:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RazaGato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gatito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField(default=1)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='')),
                ('fecha_publicacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mascota_ET.razagato')),
            ],
        ),
    ]
