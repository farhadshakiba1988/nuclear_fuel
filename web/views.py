from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from web.forms import RecepitForm


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print("UserName does not exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print(request, 'Invalid username or password')
    return render(request, 'login_registri.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def add_recepit(request):
    if request.method == 'POST':
        form = RecepitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # بعد از موفقیت آمیز بودن ذخیره، به صفحه موفقیت بروید
    else:
        form = RecepitForm()

    return render(request, 'add_recepit.html', {'form': form})