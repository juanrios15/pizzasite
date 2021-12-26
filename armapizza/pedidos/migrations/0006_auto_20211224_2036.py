# Generated by Django 3.2.9 on 2021-12-25 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_alter_pizzatradicional_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzatradicional',
            name='primera_mitad',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='direccion',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='email',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
