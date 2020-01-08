from django import template
from orders.models import Pizza, Sub

register = template.Library()

@register.filter
def hello(value):
	return value + " Hello!"

@register.filter
def get_by_id(value,pk):
	# get item object id and return all of its data...how to determine which model?
	if not Pizza.objects.filter(pk=pk):
		return "No pizza for you"
	elif not Sub.objects.filter(pk=pk):
		return "No sub for you"
	
	return f"Woooow! {pk} is here!"
		

