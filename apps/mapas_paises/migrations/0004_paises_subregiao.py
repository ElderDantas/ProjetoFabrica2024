# Generated by Django 5.1 on 2024-08-24 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapas_paises', '0003_alter_cidade_populacao_alter_paises_populacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='paises',
            name='subregiao',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
