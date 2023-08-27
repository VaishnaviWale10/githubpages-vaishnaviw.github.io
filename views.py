from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
    return render(request, 'application/index.html')

def menu(request):
    return render(request, 'application/menu.html')


def contact(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        tech = request.POST.get('Technology')
        if Subscriber.objects.filter(email=email):
            messages.info(request, "Email already used...")
            return render(request, 'application/contact.html')
        else:
            subscribe = Subscriber.objects.create(first_name=first_name, last_name=last_name, email=email,
                                                  Technology=tech)
            subscribe.save()
            messages.info(request, "Subscribed successfully!!")
            return render(request, 'application/contact.html')
    else:
        return render(request, 'application/contact.html')



def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authentificate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials...")
            return redirect('login')
    else:
        return render(request, 'application/login.html')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist...")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "email already taken...")
                return redirect('register')
            else:
                user = User.objects.creat_user(first_name=first_name, last_name=last_name, email=email,
                                               username=username, password=password1)
                user.save()
                messages.info(request, "User created successfully..")
                return redirect('login')
        else:
            messages.info(request, "Password does not match..")
            return redirect('register')
    else:
         return render(request, 'application/login.html')


def payment(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')
        if Payment.objects.filter(email=email):
            messages.info(request, "Email already used...")
            return render(request, 'application/payment.html')
        else:
            payment= Payment.objects.create(first_name=first_name, last_name=last_name, email=email,
                                                  amount=amount)
            payment.save()
            messages.info(request, "Payment done successfully!!")
            return render(request, 'application/payment.html')
    else:
         return render(request, 'application/payment.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
def about(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        tech = request.POST.get('Technology')
        if Subscriber.objects.filter(email=email):
            messages.info(request, "Email already used...")
            return render(request, 'application/about.html')
        else:
            subscribe = Subscriber.objects.create(first_name=first_name, last_name=last_name, email=email,
                                                  Technology=tech)
            subscribe.save()
            messages.info(request, "Subscribed successfully!!")
            return render(request, 'application/about.html')
    else:
        return render(request, 'application/about.html')



def order(request):
    return render(request, 'application/order.html')
