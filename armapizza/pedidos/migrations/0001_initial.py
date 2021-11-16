# Generated by Django 3.2.9 on 2021-11-15 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=250)),
                ('valor_total', models.IntegerField()),
                ('email', models.CharField(max_length=80)),
                ('celular', models.CharField(max_length=40)),
                ('usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tamano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('factorial', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_queso', models.BooleanField(default=False)),
                ('mitad_mitad', models.BooleanField(default=False)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField(default=1)),
                ('masa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.masa')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido')),
                ('queso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.queso')),
                ('tamano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.tamano')),
            ],
        ),
        migrations.CreateModel(
            name='OtrosPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.otroproducto')),
            ],
        ),
        migrations.CreateModel(
            name='IngredientesPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primera_mitad', models.BooleanField(default=True)),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.ingrediente')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pizza')),
            ],
        ),
    ]
