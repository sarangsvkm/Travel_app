from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Place, Dev


# Create your views here.
def demo(request):
    val = Place.objects.all()
    dev = Dev.objects.all()
    return render(request, 'index.html', {'object': val, 'devl': dev})

def login(request):
    if request.method== 'POST':
        user = request.POST['username']
        pswd = request.POST['password']

        user= auth.authenticate(username= user, password= pswd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')


    return render(request,'login.html')


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['password2']

        if password == c_password:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                password=password, email=email)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('register')

        return redirect('/')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
