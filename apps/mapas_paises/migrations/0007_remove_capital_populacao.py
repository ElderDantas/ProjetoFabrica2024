# Generated by Django 5.1 on 2024-08-25 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapas_paises', '0006_remove_paises_capital_capital_delete_cidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capital',
            name='populacao',
        ),
    ]
