from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import logging


# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		# logger.debug("I am here :D")
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f"Account created for {username}!")
			return redirect("index")
	else:
		form = UserCreationForm()
	return render(request, "orders/register.html", {"form": form})

def login(request):
    return HttpResponse("Project 3: Login TODO")

def logout(request):
    return HttpResponse("Project 3: Logout TODO")
