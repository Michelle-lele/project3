# Generated by Django 2.2.6 on 2019-11-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20191103_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='size',
        ),
        migrations.AddField(
            model_name='size',
            name='size',
            field=models.ManyToManyField(related_name='_size_size_+', to='orders.Size'),
        ),
    ]
