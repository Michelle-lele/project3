# Generated by Django 2.0.3 on 2019-10-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191012_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=64),
        ),
    ]
