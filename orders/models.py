from django.db import models

# Create your models here.

class abstractMenuItem(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(decimal_places=2,max_digits=10, blank=True, null=True)

	class Meta:
		abstract = True


ITEM_SIZES = (
			('S','Small'),
			('L','Large'),
			)

class Size(models.Model):
	def size_default():
		return ('S','Small')

	size = models.CharField(choices=ITEM_SIZES, max_length=1, blank=False, default=size_default())

	def __str__(self):
		return f"{self.size}"

class Topping(abstractMenuItem):
	def __str__(self):
		return f"{self.name}"

class Pizza(abstractMenuItem):
	type = models.CharField(max_length=64)
	toppings = models.ManyToManyField(Topping, blank=True)
	maxToppings =  models.IntegerField(blank=True)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.type} {self.name}, {self.maxToppings} toppings, {self.size.name}"

class Sub(abstractMenuItem):
	toppings = models.ManyToManyField(Topping, blank=True)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)

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
