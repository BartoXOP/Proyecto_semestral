# Generated by Django 4.0.4 on 2022-06-15 23:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField(default=0)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='')),
                ('stock', models.IntegerField(default=1)),
                ('disponible', models.BooleanField(default=True)),
                ('fecha_publicacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producto.marca')),
                ('tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producto.tipo_producto')),
            ],
        ),
    ]
