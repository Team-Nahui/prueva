# Generated by Django 4.0.1 on 2022-01-31 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_remove_pedido_player_id_producto_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
    ]
