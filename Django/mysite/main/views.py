from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def homepage(request):
    #return HttpResponse("pythonprogramming.net homepage! Wow so #amaze.")
    return render(request=request,
    			  template_name='main/home.html',
    			  context={'tutorials':Tutorial.objects.all})

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New account created: {username}")
			login(request, user)
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
				try:
					print(form)
				except:
					print("lel")

			return render(request=request,
						  template_name='main/register.html',
						  context={'form':form})

	form = NewUserForm
	return render(request=request,
				  template_name='main/register.html',
				  context={'form':form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now loggin as {username}")
				return redirect ('/')
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")
	form = AuthenticationForm()
	return render(request=request,
				  template_name='main/login.html',
				  context={"form":form})














