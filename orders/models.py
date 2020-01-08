from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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
	preselectedToppings = models.ManyToManyField("Topping", blank=True, verbose_name="Pre-selected Toppings")

	def clean(self):
		if self.toppingOption == '0' or self.toppingOption == '3':
			self.maxToppings = None
			#TODO figure how to clear the MM relationship here and on the below line
			self.preselectedToppings.clear()
		elif self.toppingOption == '1' or self.toppingOption == '4':
			if self.preselectedToppings is None:
				raise ValidationError(
					_('You should select at least 1 topping!')
					)
			self.maxToppings = None
		elif self.toppingOption == '2':
			if self.maxToppings is None:
				raise ValidationError({'maxToppings':
					_('Maximum Toppings is required!')
					})
			self.preselectedToppings.clear()

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

	#TODO check to see why Item object is not saved
	def save(self, *args, **kwargs):
		newItem = Item(name=self.name,price=self.price, size=self.size)
		newItem.save()
		super().save(*args, **kwargs)


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
	# order total method & attribute???
	
	def __str__(self):
		return f"Order #{self.id}"