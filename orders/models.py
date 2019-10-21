from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class abstractMenuItem(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(decimal_places=2,max_digits=10, default=0)

	class Meta:
		abstract = True

class abstractToppingConfig(models.Model):
	toppingOption = models.CharField(max_length=1, choices=(('0','No toppings'), ('1','Pre-selected'), ('2','No more than..'), ('3','Select from all')), default = ('0','No toppings'),help_text="Allow users select toppings")
	maxToppings =  models.PositiveSmallIntegerField(blank=True, null=True, default=0)
	toppings = models.ManyToManyField("Topping", blank=True)

	'''
	models.CharField(validators=[validate_comma_separated_integer_list],max_length=200, blank=True, null=True,default='')
	'''

	def configureToppings(toppingOption):
		if toppingOption == '0':
			#set maxtoppings & toppings to disabled? how?
			return 1
		elif toppingOption == '1':
			#allow admin to select from all available toppings to show only those to user. 
			#how? maxtoppings to disabled
			#toppings enabled only
			return 1
		elif toppingOption == '2':
			#admin doesn't have to preselect the toppings
			#maxtoppings to enabled only
			#toppings disabled
			return 1
		elif toppingOption == '3':
			#maxtoppings to be set to the number of toppings- disabled
			#toppings disabled
			return 1

	class Meta:
		abstract = True


class Size(models.Model):
	size = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.size}"

class pizzaType(models.Model):
	type = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.type}"

class Topping(abstractMenuItem):
	def __str__(self):
		return f"{self.name}"
 
class Pizza(abstractMenuItem, abstractToppingConfig):
	type = models.ForeignKey(pizzaType, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.type} {self.name}, {self.size}"

class Sub(abstractMenuItem):
	size = models.ForeignKey(Size, on_delete=models.CASCADE)

	additions = []

	def __str__(self):
		return f"{self.name} {self.size}"	

class Pasta(abstractMenuItem):
	def __str__(self):
		return f"{self.name}"

class Salad(abstractMenuItem):
	def __str__(self):
		return f"{self.name}"

class dinnerPlatter(abstractMenuItem):
	size = models.ForeignKey(Size, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} {self.size}"
