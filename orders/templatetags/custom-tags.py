from django import template

register = template.Library()

@register.filter
def hello(value):
	return value + " Hello!"

def get_id(value):
	# get item object id and return all of its data...how to determine which model?
	return "Data"