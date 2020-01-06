from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'Pinnochio\'s Pizza Orders'

admin.site.register(Order)
admin.site.register(orderItem)

class ToppingAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')
	fieldsets = (
		(None, {
			'fields': ('name','price')
		}),
	)

admin.site.register(Topping, ToppingAdmin)



class PizzaAdmin(admin.ModelAdmin):
	list_display = ('type','name','size','toppingOption','price')
	list_filter = ('type', 'size', 'toppingOption')
	change_form_template = 'admin/orders/orders_change_form.html'
	fieldsets = (
		(None, {
			'fields': ('name',('type', 'size'), 'price')
		}),
		('Advanced options', {
			'classes': ('collapse',),
			'fields': (('toppingOption', 'maxToppings'), 'preselectedToppings'),
		}),
	)


admin.site.register(Pizza, PizzaAdmin)

class SubAdmin(admin.ModelAdmin):
	list_display = ('name', 'size', 'toppingOption', 'price')
	list_filter = ('size',)
	change_form_template = 'admin/orders/orders_change_form.html'
	fieldsets = (
		(None, {
			'fields': ('name', 'size', 'price')
		}),
		('Advanced options', {
			'classes': ('collapse',),
			'fields': (('toppingOption', 'maxToppings'), 'preselectedToppings'),
		}),
	)

admin.site.register(Sub, SubAdmin)

class PastaAdmin(admin.ModelAdmin):
	list_display=('name','price')
	fieldsets = (
		(None, {
			'fields': ('name','price')
		}),
	)

admin.site.register(Pasta, PastaAdmin)

class SaladAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')
	fieldsets = (
		(None, {
			'fields': ('name','price')
		}),
	)

admin.site.register(Salad, SaladAdmin)

class dinnerPlatterAdmin(admin.ModelAdmin):
	list_display= ('name','size', 'price')
	list_filter = ('size',)
	fieldsets = (
		(None, {
			'fields': ('name','price')
		}),
	)

admin.site.register(dinnerPlatter, dinnerPlatterAdmin)

