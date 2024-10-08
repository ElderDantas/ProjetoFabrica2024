# Generated by Django 5.1 on 2024-08-25 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapas_paises', '0005_alter_cidade_país'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paises',
            name='capital',
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('populacao', models.IntegerField()),
                ('pais', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='capital', to='mapas_paises.paises')),
            ],
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
    ]
