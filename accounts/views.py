from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm

# Create your views here.
def index(request):
    """
    return the index.html file
    """
    return render(request, 'index.html')
    
def logout(request):
    """
    Log the user out
    """
    auth.logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect(reverse('index'))
    
def login(request):
    """
    Return the login page
    """
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user=auth.authenticate(username=request.POST['username'],
            password=request.POST['password'])
            messages.success(request, "You are now logged in")
            if user:
                auth.login(user=user, request=request)
                else:
                    login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})
    