# Generated by Django 4.2.1 on 2023-05-31 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_producto_opcion_entrega_producto_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincia',
            name='nom_prov',
            field=models.CharField(max_length=30, null=True),
        ),
    ]