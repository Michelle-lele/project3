from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

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

@login_required
def menu(request):
	return render(request, "orders/menu.html")
