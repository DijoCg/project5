from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        if not all([username, first_name, last_name, email, password, password1]):
            messages.error(request, "All fields are required")
            return redirect('register')

        if password != password1:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username taken")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email taken")
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            email=email, password=password)
            user.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')

    return render(request, 'register.html')


@login_required
def home(request):
    return render(request, 'home.html')
