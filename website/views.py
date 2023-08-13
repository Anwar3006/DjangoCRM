from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.


def homepage(request):
    """
    Handles Homepage request
    """
    records = Record.objects.all()

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
        return render(request, 'homepage.html', {'records': records})


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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and log user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered')
            return redirect('homepage')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, id):
    """
    View each customer's record
    """
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(pk=id)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(
            request, 'You must be logged in to view the requested page')
        return redirect('homepage')


def delete_record(request, id):
    """
    Delete customer record
    """
    if request.user.is_authenticated:
        get_record = Record.objects.get(pk=id)
        get_record.delete()
        messages.success(request, 'Record Successfully Deleted')
        return redirect('homepage')
    else:
        messages.success(
            request, 'You must be logged in to view the requested page')
        return redirect('homepage')


def insert_record(request):
    """
    Insert a customer record
    """
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Added')
                return redirect('homepage')
        return render(request, 'insert.html', {'form': form})
    else:
        messages.success(
            request, 'You must be logged in to view the requested page')
        return redirect('homepage')


def update_record(request, id):
    """
    Update customer records
    """
    if request.user.is_authenticated:
        get_record = Record.objects.get(pk=id)
        form = AddRecordForm(request.POST or None, instance=get_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been modified')
            return redirect('homepage')
        return render(request, 'update.html', {'form': form})
    else:
        messages.success(
            request, 'You must be logged in to view the requested page')
        return redirect('homepage')
