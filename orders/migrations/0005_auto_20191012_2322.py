# Generated by Django 2.0.3 on 2019-10-12 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191012_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='orders.Topping'),
        ),
        migrations.AlterField(
            model_name='dinnerplatter',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salad',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sub',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='topping',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
