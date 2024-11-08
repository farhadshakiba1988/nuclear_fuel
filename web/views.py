from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from web.models import Receipt

from web.forms import ReceiptForm

from web.forms import UploadFileForm


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('conf:index')

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
            return redirect('conf:index')
        else:
            print(request, 'Invalid username or password')
    return render(request, 'login_registri.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def receipt_list(request):
    receipts = Receipt.objects.all()  # علامت = استفاده کنید
    ctx = {'receipts': receipts}
    return render(request, 'data_list.html', ctx)


def save_sample_data(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conf:success_page')  # به صفحه‌ای که می‌خواهید کاربر را پس از ذخیره هدایت کنید
        else:
            print(form.errors)  # برای نمایش خطاها در صورت عدم ذخیره
    else:
        form = ReceiptForm()
    return render(request, 'your_template.html', {'form': form})


def success_page(request):
    return render(request, 'success_page.html')


def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('conf:upload_file')  # نام صفحه‌ی فعلی یا صفحه موردنظر برای ریدایرکت
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})


def chart_view(request):
    return render(request, 'chart.html')