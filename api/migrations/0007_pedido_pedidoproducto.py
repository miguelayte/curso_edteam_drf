# Generated by Django 4.2 on 2024-12-09 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_producto_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.cliente')),
                ('productos', models.ManyToManyField(to='api.producto')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='pedido_productos', to='api.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.producto')),
            ],
        ),
    ]
