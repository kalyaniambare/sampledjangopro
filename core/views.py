from django.contrib.auth import login as login_prosses, logout
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.form import UserForm, UserFormLogin
from core.models import User


@login_required
def home(request):
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        username = data.get('username')
        address = data.get('address')
        phone_number = data.get('phone_number')
        user = User.objects.get(username=request.user)
        user.email = email
        user.username = username
        user.address = address
        user.phone_number = phone_number
        user.save()
        request.session.modified = True
        user = User.objects.get(username=request.user)
        form = UserForm(instance=request.user)
        toster = True

        return render(request, 'home.html', {'user': user, 'form': form,"toster":toster})
    request.session.modified = True
    user = User.objects.get(username=request.user)
    form = UserForm(instance=request.user)
    return render(request, 'home.html', {'user': user, 'form': form})


class MyBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        user = User.objects.get(email=email, password=password)
        return user


def Signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            save = form.save()
            save.save()
            return HttpResponse("done")
    else:
        form = UserForm()
    return render(request, 'signup.html', {"form": form})


def login(request):
    if request.method == "POST":
        form = UserFormLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.get(email=email)
            user.check_password(password)
            try:
                my_way = MyBackend()
                my_way.authenticate(request, email, password)
            except:
                form = UserFormLogin()
                return render(request, 'login.html', {"form": form})
            request.session['user_id'] = user.id
            login_prosses(request, user)
            return redirect('home')
    else:
        form = UserFormLogin()
    return render(request, 'login.html', {"form": form})


def logout_view(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    logout(request)
    return render(request, 'home.html')
