# Generated by Django 2.0.3 on 2019-10-12 20:04

from django.db import migrations


class Migration(migrations.Migration):
	atomic = False

	dependencies = [
		('orders', '0002_auto_20191012_2256'),
	]

	operations = [
		migrations.RenameModel(
			old_name='Subs',
			new_name='Sub',
		),
	]
