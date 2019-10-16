from django.db import models

# Create your models here.
class abstractMenuItem(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(decimal_places=2,max_digits=10, default=0)

	class Meta:
		abstract = True

class abstractToppingConfig(models.Model):
	toppingOption = models.CharField(max_length=1, choices=(('0','No toppings'), ('1','Pre-selected'), ('2','No more than..'), ('3','Select from all')), default = ('0','No toppings'),help_text="Allow users select toppings")

	def configureToppings(toppingOption):
		if toppingOption == '0':
			pass
		if toppingOption == '2':
			maxToppings =  models.PositiveSmallIntegerField(blank=True, null=True)
			toppings = models.CharField
			return maxToppings

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
 
class Pizza(abstractMenuItem):
	type = models.ForeignKey(pizzaType, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	
	toppingConfiguration = abstractToppingConfig()
	maxToppings = toppingConfiguration.configureToppings(toppingOption)

	def __str__(self):
		return f"{self.type} {self.name}, {self.maxToppings} toppings, {self.size}"

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
