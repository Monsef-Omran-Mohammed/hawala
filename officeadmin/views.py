from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from account.models import TblUser, TblOfficeUser, CITY_CHOICES
from office.models import TblOfficePhone
from account.forms import OfficeSignUpForm
from officeadmin.forms import OfficeEmailUpdateForm, OfficePhoneUpdateForm, OfficeActiveUpdateForm
# Create your views here.
is_officeadmin = 0

def home(r):
    return render(r, 'officeadmin/home.html', {})


@login_required(login_url='account:logout')
def createOffice(request):
    if request.user.user_type != is_officeadmin:
        return redirect('account:logout')

    if request.method == 'POST':
        form = OfficeSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('officeadmin:offices-list')
    else:
        form = OfficeSignUpForm()
    context = {
        'title': 'create-office',
        'form': form,
    }
    return render(request, 'officeadmin/createOffice.html', context)


@login_required(login_url='account:logout')
def officesList(request):
    if request.user.user_type != is_officeadmin:
        return redirect('account:logout')
    
    if request.method == 'GET':
        city = request.GET.get('city')
        if city == None or city=='':
            offices = TblOfficeUser.objects.all().order_by('-create_at')
        else:
            offices = TblOfficeUser.objects.filter(city=city).order_by('-create_at')
        paginator = Paginator(offices, 25)
        page_num = request.GET.get('page', 1)
        try:
            offices = paginator.page(page_num)
        except PageNotAnInteger:
            offices = paginator.page(1)
        except EmptyPage:
            offices = paginator.page(paginator.num_pages)

    context = {
        'title': 'offices-list',
        'offices': offices,
        'CITY_CHOICES': CITY_CHOICES,
    }
    return render(request, 'officeadmin/officesList.html', context)


@login_required(login_url='account:logout')
def office(request, office_id):
    if request.user.user_type != is_officeadmin:
        return redirect('account:logout')
    
    office = get_object_or_404(TblOfficeUser, pk=office_id)
    phone_numbers = TblOfficePhone.objects.filter(office=office_id)

    context = {
        'parentTitle': 'offices-list',
        'title': 'office',
        'office': office,
        'CITY_CHOICES': CITY_CHOICES,
        'phone_numbers': phone_numbers,
    }
    return render(request, 'officeadmin/office.html', context)


# تعديل البريد الالكتروني الرئيسية للقسم
@login_required(login_url='account:logout')
def officeEmailUpdate(request, office_id):
    if request.user.user_type != is_officeadmin:
        return redirect('account:logout')

    data = get_object_or_404(TblUser, pk=office_id)
    form = OfficeEmailUpdateForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = OfficeEmailUpdateForm(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            fd = form.save(commit=False)
            fd.save()
            return redirect(f'../{office_id}')
    context = {
        'parentTitle': 'office',
        'title': 'office-email-update',
        'form': form,
    }
    return render(request, 'officeadmin/officeEmailUpdate.html', context)


# تعديل رقم هاتف الرئيسية للقسم
@login_required(login_url='account:logout')
def officePhoneUpdate(request, office_id):
    if request.user.user_type != is_officeadmin:
        return redirect('account:logout')

    data = get_object_or_404(TblOfficeUser, pk=office_id)
    form = OfficePhoneUpdateForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = OfficePhoneUpdateForm(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            fd = form.save(commit=False)
            fd.save()
            return redirect(f'../{office_id}')
    context = {
        'parentTitle': 'office',
        'title': 'office-phone-update',
        'form': form,
    }
    return render(request, 'officeadmin/officePhoneUpdate.html', context)


# تعديل حالة حساب المكتب : نشط او غير نشط
@login_required(login_url='account:logout')
def officeActiveUpdate(request, office_id):
    if request.user.user_type != is_officeadmin:
        return redirect('account:logout')

    data = get_object_or_404(TblUser, pk=office_id)
    form = OfficeActiveUpdateForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = OfficeActiveUpdateForm(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            fd = form.save(commit=False)
            fd.save()
            return redirect(f'../{office_id}')
    context = {
        'parentTitle': 'office',
        'title': 'office-active-update',
        'form': form,
    }
    return render(request, 'officeadmin/officeActiveUpdate.html', context)




