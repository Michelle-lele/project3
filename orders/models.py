from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.
class abstractMenuItem(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(decimal_places=2,max_digits=10, default=0)

	class Meta:
		abstract = True

class abstractToppingConfig(models.Model):
	toppingOption = models.CharField(max_length=1, choices=(('0','No toppings'), ('1','Pre-selected'), ('2','No more than..'), ('3','Select from all'), ('4', 'Additions')), default = ('0','No toppings'),help_text="Allow users select toppings", verbose_name = "Topping Options")
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


class Size(models.Model):
	size = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.size}"

class pizzaType(models.Model):
	type = models.CharField(max_length=64, verbose_name = "Pizza type")

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

class Sub(abstractMenuItem,abstractToppingConfig):
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
