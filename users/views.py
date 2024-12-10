from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache

from .forms import UserRegistrationForm

from .models import CustomUser

# Create your views here.

def register(request):
    if request.method == "POST":
        user_registration_form = UserRegistrationForm(request.POST)

        email = request.POST.get("email")
        username = request.POST.get("username")
        
        # Check if email or username already exists
        if CustomUser.objects.filter(email=email).exists():
            print("A user is already registered with this email.")
        elif CustomUser.objects.filter(username=username).exists():
            print("A user is already registered with this username.")
        else:
            # Register the user to the database
            user_registration_form.save()
            return render(request, "auth/login.html", {})
    else:
        if request.user.is_authenticated:  
            return redirect('home')
        else:
            return render(request, "auth/register.html", {})


@never_cache
def login(request):

    # Sign in process
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        users = CustomUser.objects.filter(username=username,password=password)

        if users.exists():
            return redirect('home')  
        else:
              print("not found")

    else:
        # Check if the user already logged in 
        if request.user.is_authenticated:  
            return redirect('home')
        else:
            # Rendering the login page
            return render(request,"auth/login.html",{})
   
