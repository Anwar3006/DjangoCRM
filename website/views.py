from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def homepage(request):
    """
    Handles Homepage request
    """
    # Check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('homepage')
        else:
            messages.success(
                request, 'There was an error logging in, please try again')
            return redirect('homepage')
    else:
        return render(request, 'homepage.html', {})


def logout_user(request):
    """
    Logout a user
    """
    logout(request)
    messages.success(
        request, 'You have logged out')
    return redirect('homepage')


def register_user(request):
    """
    Register users
    """
    return render(request, 'register.html', {})
