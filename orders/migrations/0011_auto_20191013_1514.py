# Generated by Django 2.0.3 on 2019-10-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20191013_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('L', 'Large')], default='S', max_length=1),
        ),
    ]