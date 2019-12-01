# Generated by Django 2.2.6 on 2019-11-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_auto_20191112_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='size',
        ),
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.ManyToManyField(to='orders.Size'),
        ),
        migrations.RemoveField(
            model_name='size',
            name='size',
        ),
        migrations.AddField(
            model_name='size',
            name='size',
            field=models.CharField(default='Regular', max_length=64),
        ),
    ]