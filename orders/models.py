from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User

SIZES = (
	('R','Regular'),
	('S','Small'),
	('L','Large')
	)

class Item(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(decimal_places=2,max_digits=10, default=0)
	size = models.CharField(choices=SIZES, max_length=64, default="R")

	def __str__(self):
		return f"{self.name}, {self.size}, ${self.price}"

TOPPING_OPTIONS = (
	('0','No toppings'), 
	('1','Pre-selected'), 
	('2','No more than..'), 
	('3','Select from all'), 
	('4','Additions')
	)

class abstractToppingConfig(models.Model):
	toppingOption = models.CharField(max_length=1, 
		choices= TOPPING_OPTIONS,
		default = ('0','No toppings'),
		help_text="Allow users to select toppings", 
		verbose_name = "Topping Options")
	maxToppings =  models.PositiveSmallIntegerField(blank=True, null=True, default=0, verbose_name = "Max. toppings")
	toppings = models.ManyToManyField("Topping", blank=True)

	'''TODO validation of the toppings data on object init/update how?
		if toppingOption == '0' or toppingOption == '3':
			#set maxtoppings & toppings to null
		elif toppingOption == '1' or toppingOption == '4':
			# maxtoppings to null
			# toppings is required
		elif toppingOption == '2':
			#admin doesn't have to preselect the toppings
			#maxtoppings is required
			#toppings to null
	'''
	class Meta:
		abstract = True

class pizzaType(models.Model):
	type = models.CharField(max_length=64, verbose_name = "Pizza type")

	def __str__(self):
		return f"{self.type}"

class Topping(Item):
	def __str__(self):
		return f"{self.name}"
 
class Pizza(Item, abstractToppingConfig):
	type = models.ForeignKey(pizzaType, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.type} {self.name}, {self.size}"

class Sub(Item, abstractToppingConfig):

	def __str__(self):
		return f"{self.name} {self.size}"	

class Pasta(Item):
	def __str__(self):
		return f"{self.name}"

class Salad(Item):
	def __str__(self):
		return f"{self.name}"

class dinnerPlatter(Item):

	def __str__(self):
		return f"{self.name} {self.size}"

class orderItem(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	hasToppings = models.ManyToManyField("Topping", blank=True, related_name="hasToppings")
	hasAdditions = models.ManyToManyField("Topping", blank=True, related_name = "hasAdditions")

	def __str__(self):
		return f"{self.quantity} X {self.item}"

class Order(models.Model):
	orderItem = models.ManyToManyField("orderItem")
	orderedDate = models.DateTimeField(blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	startDate = models.DateTimeField(auto_now_add = True)
	ordered = models.BooleanField(default="False")
	# order total???
	
	def __str__(self):
		return f"Order #{self.id}"