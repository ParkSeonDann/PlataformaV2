# Generated by Django 4.2.1 on 2023-05-31 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_guia_despacho_fecha_producto_cantidad_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='id_prod',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='id_boleta',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='total_pago',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='boleta_detalle',
            name='cantidad',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='boleta_detalle',
            name='id_boleta_det',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='boleta_detalle',
            name='precio',
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name='boleta_detalle',
            name='total',
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name='camion',
            name='cantidad_prod',
            field=models.IntegerField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='camion',
            name='id_camion',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='id_cargo',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='num_cel',
            field=models.IntegerField(max_length=9),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut_cli',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='color',
            name='id_color',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='compra',
            name='id_compra',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='compra',
            name='total_pago',
            field=models.IntegerField(max_length=8),
        ),
        migrations.AlterField(
            model_name='compra_det',
            name='cantidad',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='compra_det',
            name='id_compra',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='compra_det',
            name='precio',
            field=models.IntegerField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='compra_det',
            name='total',
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name='comuna',
            name='id_com',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='conductor',
            name='id_conduc',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='conductor',
            name='rut_con',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='id_emp',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='salario',
            field=models.IntegerField(max_length=7),
        ),
        migrations.AlterField(
            model_name='espacio_bodega',
            name='fila',
            field=models.IntegerField(max_length=7),
        ),
        migrations.AlterField(
            model_name='espacio_bodega',
            name='id_espacio',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='espacio_bodega',
            name='stock',
            field=models.IntegerField(max_length=7),
        ),
        migrations.AlterField(
            model_name='especie',
            name='id_esp',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fertilizante',
            name='id_fer',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gd_detalle',
            name='cantidad',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='gd_detalle',
            name='id_gd',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gd_detalle',
            name='precio',
            field=models.IntegerField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='gd_detalle',
            name='total',
            field=models.IntegerField(max_length=12),
        ),
        migrations.AlterField(
            model_name='guia_despacho',
            name='id_gd',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='localizacion',
            name='id_localizacion',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='macetero',
            name='id_macetero',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='macetero',
            name='precio',
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='pais',
            name='id_pais',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='planta',
            name='id_planta',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='planta',
            name='precio',
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad_prod',
            field=models.IntegerField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_prod',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='id_prov',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='id_prov',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='id_region',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='id_ruta',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='id_sucursal',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='temporada',
            name='id_temp',
            field=models.IntegerField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipo_pago',
            name='id_tipo_pago',
            field=models.IntegerField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipofer',
            name='id_tipo_Fer',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipofer',
            name='precio',
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='id_tipo',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
    ]