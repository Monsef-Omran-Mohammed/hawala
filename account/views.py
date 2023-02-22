from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import OfficeSignUpForm, OfficeUserForm
from .models import TblUser, TblOfficeUser
# Create your views here.

def office_register(request):
    if request.method == 'POST':
        form = OfficeSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('account:office-users')
    else:
        form = OfficeSignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'account/officeRegister.html', context)


def office_users(request):
    user = TblUser.objects.filter(user_type=1)

    context = {
        'user': user,
    }
    return render(request, 'account/officeUsers.html', context)


def office_user_page(request, pk):
    data = get_object_or_404(TblOfficeUser, pk=pk)
    context = {
        'data': data,
    }
    return render(request, 'account/officeUserPage.html', context)


def office_user_update(request, pk):
    data = get_object_or_404(TblOfficeUser, pk=pk)
    form = OfficeUserForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = OfficeUserForm(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            fd = form.save(commit=False)
            fd.save()
            return redirect('../')
    context = {
        'form': form,
    }
    return render(request, 'account/officeUserUpdate.html', context)


'''
# ========== [ Login & Logout ] ========== #
'''

def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                if user.user_type == 0:
                    return redirect('officeadmin:home')
                elif user.user_type == 1:
                    return redirect('office:outgoing-transfers-list')
                else:
                    return redirect('account:logout')
            else:
                messages.warning(request, 'خطأ في اسم المستخدم أو كلمة مرور', extra_tags='alert alert-danger')
        else:
                messages.warning(request, 'خطأ في اسم المستخدم أو كلمة مرور', extra_tags='alert alert-danger')
    context={
        'form':AuthenticationForm(),
    }
    return render(request, 'account/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('account:login')