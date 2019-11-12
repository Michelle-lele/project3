from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import pizzaType, Size, Pizza, Sub

import logging

# Create your views here.
@login_required
def index(request):
	pizzaTypes = pizzaType.objects.all()
	sizes = Size.objects.all()
	pizzas = Pizza.objects.all()
	subs = Sub.objects.all()
	return render(request, "orders/index.html",
		{'pizzaTypes': pizzaTypes,
		'sizes': sizes,
		'pizzas': pizzas,
		'subs': subs},)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		# logger.debug("I am here :D")
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"Account created for {username}!")
			return redirect("login")
	else:
		form = UserRegisterForm()
	return render(request, "orders/register.html", {"form": form})
	