from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import CreateUserForm


@unauthenticated_user
def loging_or_register(request):
    form = CreateUserForm()
    contex = {'form': form}
    return render(request, 'email_sender/login_or_register.html', contex)


@unauthenticated_user
def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'{username} created successfully')
            return login_user(request)
        else:
            for m in form.errors:
                messages.error(request, form.errors[m])
            contex = {'form': form, 'register': 'true'}
            return render(request, 'email_sender/login_or_register.html', contex)
    else:
        return redirect('login_or_register')


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login_or_register')
    else:
        return redirect('login_or_register')


def logout_user(request):
    logout(request)
    return redirect('login_or_register')


@login_required(login_url='login_or_register')
@admin_only
def index(request):
    contex = {"user": request.user}
    return render(request, 'email_sender/basic_dashboard.html', contex)


@login_required(login_url='login_or_register')
@allowed_users(allowed_roles=[None])
def user_page(request):
    contex = {"user": request.user}
    return render(request, 'email_sender/user_page.html', contex)
