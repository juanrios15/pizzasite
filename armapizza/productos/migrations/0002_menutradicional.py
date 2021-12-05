# Generated by Django 3.2.9 on 2021-11-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuTradicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='media')),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
    ]
