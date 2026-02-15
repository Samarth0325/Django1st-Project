from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, "Authentication/index.html")

def signup(request):

    if request.method == "POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        password=request.POST["pass1"]
        password2=request.POST["pass2"]


        myuser = User.objects.create_user(username, email, password)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        messages.success(request, "your account has been created successfully.")
    
        return redirect('signin')



    return render(request, "Authentication/signup.html")


def signin(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass1"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, "authentication/index.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect("home")


    return render(request, "Authentication/signin.html")

def signout(request):
    pass