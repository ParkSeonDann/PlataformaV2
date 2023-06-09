# Generated by Django 4.0.4 on 2023-05-05 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id_cargo', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_cargo', models.CharField(max_length=30)),
                ('min_salario', models.IntegerField(verbose_name=4)),
                ('max_salario', models.IntegerField(verbose_name=7)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut_cli', models.IntegerField(primary_key=True, serialize=False, verbose_name=10)),
                ('nom_cli', models.CharField(max_length=30)),
                ('app_cli', models.CharField(max_length=30)),
                ('raz_sol', models.CharField(max_length=30)),
                ('num_cel', models.IntegerField(verbose_name=9)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id_color', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_color', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_com', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_com', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id_conduc', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_con', models.CharField(max_length=30, null=True)),
                ('apellido_con', models.CharField(max_length=30, null=True)),
                ('rut_con', models.IntegerField(null=True, verbose_name=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_emp', models.IntegerField(primary_key=True, serialize=False, verbose_name=10)),
                ('rut', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=30)),
                ('app', models.CharField(max_length=30)),
                ('apm', models.CharField(max_length=30)),
                ('num_celu', models.CharField(max_length=12)),
                ('salario', models.IntegerField(verbose_name=7)),
                ('id_cargo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id_esp', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_esp', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Localizacion',
            fields=[
                ('id_localizacion', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('direccion', models.CharField(max_length=50)),
                ('cod_postal', models.CharField(max_length=15)),
                ('id_com', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_pais', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_prod', models.CharField(max_length=30, null=True)),
                ('precio', models.IntegerField(null=True, verbose_name=6)),
                ('id_color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.color')),
            ],
        ),
        migrations.CreateModel(
            name='Temporada',
            fields=[
                ('id_temp', models.IntegerField(primary_key=True, serialize=False, verbose_name=2)),
                ('temporada', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_pago',
            fields=[
                ('id_tipo_pago', models.IntegerField(primary_key=True, serialize=False, verbose_name=2)),
                ('nom_tipo_pago', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoFer',
            fields=[
                ('id_tipo_Fer', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('tipo_fer', models.CharField(max_length=30)),
                ('especificacion', models.CharField(max_length=200)),
                ('precio', models.IntegerField(verbose_name=6)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('especificacion', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_sucursal', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('id_localizacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.localizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id_ruta', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('id_localizacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.localizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_region', models.CharField(max_length=15)),
                ('id_pais', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id_prov', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_prov', models.CharField(max_length=15)),
                ('id_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.region')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_prov', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_prov', models.CharField(max_length=20)),
                ('id_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='id_tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.tipoproducto'),
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id_planta', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_planta', models.CharField(max_length=20)),
                ('precio', models.IntegerField(verbose_name=6)),
                ('id_color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.color')),
                ('id_esp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.especie')),
                ('id_temp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.temporada')),
            ],
        ),
        migrations.CreateModel(
            name='Macetero',
            fields=[
                ('id_macetero', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('tipo_macetero', models.CharField(max_length=15)),
                ('tamanno', models.CharField(max_length=20)),
                ('precio', models.IntegerField(verbose_name=6)),
                ('id_color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.color')),
            ],
        ),
        migrations.CreateModel(
            name='Guia_Despacho',
            fields=[
                ('id_gd', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('total_pago', models.IntegerField(verbose_name=8)),
                ('id_emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.empleado')),
                ('id_sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.sucursal')),
                ('id_tipo_pago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.tipo_pago')),
                ('rut_cli', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Gd_detalle',
            fields=[
                ('id_gd', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('precio', models.IntegerField(null=True, verbose_name=6)),
                ('cantidad', models.IntegerField(verbose_name=3)),
                ('total', models.IntegerField(verbose_name=12)),
                ('id_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizante',
            fields=[
                ('id_fer', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('nom_fer', models.CharField(max_length=20)),
                ('Tipo_fer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.tipofer')),
            ],
        ),
        migrations.CreateModel(
            name='Espacio_Bodega',
            fields=[
                ('id_espacio', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('fila', models.IntegerField(verbose_name=7)),
                ('columna', models.CharField(max_length=7)),
                ('stock', models.IntegerField(verbose_name=7)),
                ('especificacion', models.CharField(max_length=200, null=True)),
                ('id_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='id_localizacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.localizacion'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='id_sucursal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.sucursal'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='id_prov',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.provincia'),
        ),
        migrations.CreateModel(
            name='Compra_det',
            fields=[
                ('id_compra', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('precio', models.IntegerField(null=True, verbose_name=6)),
                ('cantidad', models.IntegerField(verbose_name=3)),
                ('total', models.IntegerField(verbose_name=12)),
                ('id_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('total_pago', models.IntegerField(verbose_name=8)),
                ('id_emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.empleado')),
                ('id_sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.sucursal')),
                ('id_tipo_pago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.tipo_pago')),
                ('rut_cli', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_localizacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.localizacion'),
        ),
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id_camion', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('patente', models.CharField(max_length=8, null=True)),
                ('cantidad_prod', models.IntegerField(null=True, verbose_name=7)),
                ('id_conduc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.conductor')),
                ('id_ruta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.localizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta_Detalle',
            fields=[
                ('id_boleta_det', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('precio', models.IntegerField(verbose_name=12)),
                ('cantidad', models.IntegerField(verbose_name=3)),
                ('total', models.IntegerField(verbose_name=12)),
                ('id_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('total_pago', models.IntegerField(verbose_name=8)),
                ('id_emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.empleado')),
                ('id_sucursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.sucursal')),
                ('id_tipo_pago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.tipo_pago')),
                ('rut_cli', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id_prod', models.IntegerField(primary_key=True, serialize=False, verbose_name=3)),
                ('id_com', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.comuna')),
                ('id_espacio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.espacio_bodega')),
                ('id_localizacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.localizacion')),
                ('id_tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.tipoproducto')),
            ],
        ),
    ]
