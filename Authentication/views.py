from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "Authentication/index.html")

def signup(request):

    if request.method == "POST":
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]


        myuser = User.objects.create_user(username, email, password)
        myuser.first_name=fname
        myuser.last_name_name=lname

        myuser.save()

        messages.success(request, "your account has been created successfully.")
    
        return redirect('signin')




    return render(request, "Authentication/signup.html")


def signin(request):
    return render(request, "Authentication/signin.html")

def signout(request):
    pass