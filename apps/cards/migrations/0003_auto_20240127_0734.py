# Generated by Django 3.1.7 on 2024-01-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20240127_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='currency',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='multiple_use',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='restriction',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='transmitter',
            field=models.CharField(choices=[('Sucursal', 'Sucursal'), ('Línea', 'Línea')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(choices=[('Física', 'Física'), ('Digital', 'Digital')], max_length=100, null=True),
        ),
    ]