from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from account.models import TblUser, CITY_CHOICES
from .models import TblMoneyTransfer, TblOfficePhone
from .forms import (
    ApprovalMoneyTransferForm, MoneyTransferForm, 
    RejectionMoneyTransferForm, ApprovalMoneyTransferForm, 
    CreateMoneyTransferForm, OfficeProfileUpdateForm, ChangeOfficePasswordForm,
    PhoneNumberForm
)
from account.models import TblOfficeUser
# Create your views here.
is_office = 1


# قائمة الحوالات الصادرة
@login_required(login_url='account:logout')
def outgoingTransfersList(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    transfers = TblMoneyTransfer.objects.filter(sender_office=request.user.pk).order_by('-sent_at')
    paginator = Paginator(transfers, 5)
    page_num = request.GET.get('page', 1)
    try:
        transfers = paginator.page(page_num)
    except PageNotAnInteger:
        transfers = paginator.page(1)
    except EmptyPage:
        transfers = paginator.page(paginator.num_pages)

    context = {
        'parentTitle': 'outgoing-transfers',
        'title': 'outgoing-transfers-list',
        'transfers': transfers,
    }
    return render(request, 'office/outgoingTransfers/outgoingTransfersList.html', context)


# قائمة الحوالات الصادرة الموافق عليها 
@login_required(login_url='account:logout')
def doneOutgoingTransfersList(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    transfers = TblMoneyTransfer.objects.filter(sender_office=request.user.pk, approval_by_recipient=True).order_by('-approval_at')
    paginator = Paginator(transfers, 25)
    page_num = request.GET.get('page', 1)
    try:
        transfers = paginator.page(page_num)
    except PageNotAnInteger:
        transfers = paginator.page(1)
    except EmptyPage:
        transfers = paginator.page(paginator.num_pages)

    context = {
        'parentTitle': 'outgoing-transfers',
        'title': 'done-outgoing-transfers-list',
        'transfers': transfers,
    }
    return render(request, 'office/outgoingTransfers/doneOutgoingTransfersList.html', context)


# قائمة الحوالات الصادرة المعلقة 
@login_required(login_url='account:logout')
def waitingOutgoingTransfersList(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    transfers = TblMoneyTransfer.objects.filter(sender_office=request.user.pk, approval_by_recipient=False, rejection=False).order_by('-sent_at')
    paginator = Paginator(transfers, 25)
    page_num = request.GET.get('page', 1)
    try:
        transfers = paginator.page(page_num)
    except PageNotAnInteger:
        transfers = paginator.page(1)
    except EmptyPage:
        transfers = paginator.page(paginator.num_pages)

    context = {
        'parentTitle': 'outgoing-transfers',
        'title': 'waiting-outgoing-transfers-list',
        'transfers': transfers,
    }
    return render(request, 'office/outgoingTransfers/waitingOutgoingTransfersList.html', context)


# قائمة الحوالات الصادرة المرفوضة 
@login_required(login_url='account:logout')
def rejectedOutgoingTransfersList(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    transfers = TblMoneyTransfer.objects.filter(sender_office=request.user.pk, rejection=True).order_by('-rejection_at')
    paginator = Paginator(transfers, 25)
    page_num = request.GET.get('page', 1)
    try:
        transfers = paginator.page(page_num)
    except PageNotAnInteger:
        transfers = paginator.page(1)
    except EmptyPage:
        transfers = paginator.page(paginator.num_pages)

    context = {
        'parentTitle': 'outgoing-transfers',
        'title': 'rejected-outgoing-transfers-list',
        'transfers': transfers,
    }
    return render(request, 'office/outgoingTransfers/rejectedOutgoingTransfersList.html', context)


# الحوالة الصادرة
@login_required(login_url='account:logout')
def outgoingMoneyOrder(request, money_order_id):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    outgoing_money_order = get_object_or_404(TblMoneyTransfer, pk=money_order_id, sender_office=request.user.pk)
    print(outgoing_money_order.note)
    context = {
        'parentTitle': 'outgoing-transfers',
        'title': 'outgoing-money-order',
        'outgoing_money_order':outgoing_money_order,
    }
    return render(request, 'office/outgoingTransfers/outgoingMoneyOrder.html', context)


'''
=============================================================================================
=============================================================================================
=============================================================================================
=============================================================================================
=============================================================================================
'''


# قائمة الحوالات الواردة
@login_required(login_url='account:logout')
def incomingTransfersList(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    transfers = TblMoneyTransfer.objects.filter(recipient_office=request.user.pk).order_by('-sent_at')
    paginator = Paginator(transfers, 25)
    page_num = request.GET.get('page', 1)
    try:
        transfers = paginator.page(page_num)
    except PageNotAnInteger:
        transfers = paginator.page(1)
    except EmptyPage:
        transfers = paginator.page(paginator.num_pages)
    context = {
        'parentTitle': 'incoming-transfers',
        'title': 'incoming-transfers-list',
        'transfers': transfers,
    }
    return render(request, 'office/incomingTransfers/incomingTransfersList.html', context)


# قائمة الحوالات الواردةالموافق عليها
@login_required(login_url='account:logout')
def doneIncomingTransfersList(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    transfers = TblMoneyTransfer.objects.filter(recipient_office=request.user.pk, approval_by_recipient=True).order_by('-approval_at')
    paginator = Paginator(transfers, 25)
    page_num = request.GET.get('page', 1)
    try:
        transfers = paginator.page(page_num)
    except PageNotAnInteger:
        transfers = paginator.page(1)
    except EmptyPage:
        transfers = paginator.page(paginator.num_pages)
    context = {
        'parentTitle': 'incoming-transfers',
        'title': 'done-incoming-transfers-list',
        'transfers': transfers,
    }
    return render(request, 'office/incomingTransfers/doneIncomingTransfersList.html', context)


# قائمة الحوالات الواردةالمعلقة
@login_required(login_url='account:logout')
def waitingIncomingTransfersList(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    transfers = TblMoneyTransfer.objects.filter(recipient_office=request.user.pk, approval_by_recipient=False, rejection=False).order_by('-sent_at')
    paginator = Paginator(transfers, 25)
    page_num = request.GET.get('page', 1)
    try:
        transfers = paginator.page(page_num)
    except PageNotAnInteger:
        transfers = paginator.page(1)
    except EmptyPage:
        transfers = paginator.page(paginator.num_pages)
    context = {
        'parentTitle': 'incoming-transfers',
        'title': 'waiting-incoming-transfers-list',
        'transfers': transfers,
    }
    return render(request, 'office/incomingTransfers/waitingIncomingTransfersList.html', context)


# قائمة الحوالات الواردة المرفوضة
@login_required(login_url='account:logout')
def rejectedIncomingTransfersList(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    transfers = TblMoneyTransfer.objects.filter(recipient_office=request.user.pk, rejection=True).order_by('-rejection_at')
    paginator = Paginator(transfers, 25)
    page_num = request.GET.get('page', 1)
    try:
        transfers = paginator.page(page_num)
    except PageNotAnInteger:
        transfers = paginator.page(1)
    except EmptyPage:
        transfers = paginator.page(paginator.num_pages)

    context = {
        'parentTitle': 'incoming-transfers',
        'title': 'rejected-incoming-transfers-list',
        'transfers': transfers,
    }
    return render(request, 'office/incomingTransfers/rejectedIncomingTransfersList.html', context)


# الحوالة الواردة
@login_required(login_url='account:logout')
def incomingMoneyOrder(request, money_order_id):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    incoming_money_order = get_object_or_404(TblMoneyTransfer, pk=money_order_id, recipient_office=request.user.pk)
    context = {
        'parentTitle': 'incoming-transfers',
        'title': 'incoming-money-order',
        'incoming_money_order':incoming_money_order,
    }
    return render(request, 'office/incomingTransfers/incomingMoneyOrder.html', context)


# الموافقة على الحوالة
@login_required(login_url='account:logout')
def approvalMoneyTransfer(request, money_order_id):
    if request.user.user_type != is_office:
        return redirect('account:logout')

    money_transfer = get_object_or_404(TblMoneyTransfer, pk=money_order_id, recipient_office=request.user.pk, approval_by_recipient = False, rejection=False)
    if money_transfer.approval_by_recipient == False:
        form = ApprovalMoneyTransferForm(request.POST or None, instance=money_transfer)
        if request.method == 'POST':
            form = ApprovalMoneyTransferForm(request.POST or None, request.FILES or None, instance=money_transfer)
            if form.is_valid():
                fd = form.save(commit=False)
                fd.approval_at = datetime.now()
                fd.save()
                return redirect('office:done-incoming-transfers-list')
        context = {
            'form': form,
            'parentTitle': 'incoming-transfers',
            'title': 'approval-money-transfer',
        }
        return render(request, 'office/incomingTransfers/approvalMoneyTransfer.html', context)
    else:
        return redirect('office:incoming-transfers-list')


# رفض الحوالة
@login_required(login_url='account:logout')
def rejectionMoneyTransfer(request, money_order_id):
    if request.user.user_type != is_office:
        return redirect('account:logout')

    money_transfer = get_object_or_404(TblMoneyTransfer, pk=money_order_id, recipient_office=request.user.pk, approval_by_recipient = False, rejection=False)
    if money_transfer.rejection == False:
        form = RejectionMoneyTransferForm(request.POST or None, instance=money_transfer)
        if request.method == 'POST':
            form = RejectionMoneyTransferForm(request.POST or None, request.FILES or None, instance=money_transfer)
            if form.is_valid():
                post = form.save(commit=False)
                post.rejection_at = datetime.now()
                post.save()
                return redirect('office:rejected-incoming-transfers-list')
        context = {
            'form': form,
            'parentTitle': 'incoming-transfers',
            'title': 'sender-request',
        }
        return render(request, 'office/incomingTransfers/rejectionMoneyTransfer.html', context)
    else:
        return redirect('office:incoming-transfers-list')


'''
===========================================================================================
===========================================================================================
===========================================================================================
===========================================================================================
===========================================================================================
'''

# قائمة المكاتب
@login_required(login_url='account:logout')
def officeList(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')

    if request.method == 'GET':
        city = request.GET.get('city')
        if city == None or city=='':
            offices = TblOfficeUser.objects.exclude(user=request.user.pk).order_by('-create_at')
        else:
            offices = TblOfficeUser.objects.filter(city=city).exclude(user=request.user.pk).order_by('-create_at')
        paginator = Paginator(offices, 25)
        page_num = request.GET.get('page', 1)
        try:
            offices = paginator.page(page_num)
        except PageNotAnInteger:
            offices = paginator.page(1)
        except EmptyPage:
            offices = paginator.page(paginator.num_pages)

    context = {
        'parentTitle': 'office-list',
        'title': 'office-list',
        'offices': offices,
        'CITY_CHOICES': CITY_CHOICES
    }
    return render(request, 'office/officeList.html', context)


# from heyoo import WhatsApp
# المكتب
@login_required(login_url='account:logout')
def office(request, office_id):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    sender_office = get_object_or_404(TblOfficeUser, pk=request.user.pk)
    recipient_office = get_object_or_404(TblOfficeUser, pk=office_id)
    phone_numbers = TblOfficePhone.objects.filter(office=office_id)
    if request.method == 'POST':
        sender_commission = request.POST.get('sender_commission')
        recipient_commission = request.POST.get('recipient_commission')
        commission_from_sender = float(sender_commission) * 0.01
        commission_from_recipient = float(recipient_commission) * 0.01
        form = CreateMoneyTransferForm(request.POST, request.FILES)
        if form.is_valid():
            fd = form.save(commit=False)
            fd.sender_office = sender_office
            fd.recipient_office = recipient_office
            fd.commission_from_sender = commission_from_sender
            fd.commission_from_recipient = commission_from_recipient
            fd.save()

            # messenger = WhatsApp('EAAI11bNUZByoBAFAlvdGVZCWuay3XVXJX9xhpzZCrMoFwg9jnJu583Usr9u2YCSDoZAUculO3cF4ECkStZBZBAN8KZA7gtauC2o9mzRZCrIcZB5R57ZC6iuJ9LZAEXVzs3jYabYK0ebV6Ywqslfm4Wr6o1EbiPtNt9qSDquvpsz5i5JzKOziUyPEGLzXMl6tmhAz3jigoGLYZA5YMwZDZD',phone_number_id='+218913528584')
            # messenger.send_message('Hello I am WhatsApp Cloud API', '+218944479764')
            
            return redirect('office:outgoing-transfers-list')
    else:
        form = CreateMoneyTransferForm()

    context = {
        'parentTitle': 'office-list',
        'title': 'office',
        'office': recipient_office,
        'CITY_CHOICES': CITY_CHOICES,
        'phone_numbers': phone_numbers,
        'form': form,
    }
    return render(request, 'office/office.html', context)


# الملف الشخصي للمكتب
@login_required(login_url='account:logout')
def officeProfile(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')

    profile = get_object_or_404(TblOfficeUser, pk=request.user.pk)
    phone_numbers = TblOfficePhone.objects.filter(office=request.user.pk)
    context = {
        'title': 'office-profile',
        'profile': profile,
        'CITY_CHOICES': CITY_CHOICES,
        'phone_numbers': phone_numbers,
    }
    return render(request, 'office/officeProfile.html', context)


# تعديل بيانات الملف الشخصي للمكتب
@login_required(login_url='account:logout')
def officeProfileUpdate(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')

    data = get_object_or_404(TblOfficeUser, pk=request.user.pk)
    form = OfficeProfileUpdateForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = OfficeProfileUpdateForm(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            fd = form.save(commit=False)
            print("START2")
            fd.save()
            return redirect('office:office-profile')
    context = {
        'parentTitle': 'office-profile',
        'title': 'office-profile-update',
        'form': form,
    }
    return render(request, 'office/officeProfileUpdate.html', context)


# تغيير كلمة مرور حساب المكتب
class ChangeOfficePassword(PasswordChangeView):
    form_class = ChangeOfficePasswordForm
    success_url = reverse_lazy('office:office-profile')
    template_name = 'office/changeOfficePassword.html'
    extra_context = {
        'parentTitle': 'office-profile',
        'title': 'change-office-password',
    }


# انشاء رقم هاتف جديد للقسم
@login_required(login_url='account:logout')
def createOfficePhoneNumber(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    office = get_object_or_404(TblOfficeUser, pk=request.user.pk)
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST, request.FILES)
        if form.is_valid():
            fd = form.save(commit=False)
            fd.office = office
            fd.save()
            return redirect('office:office-profile')
    else:
        form = PhoneNumberForm()
    context = {
        'parentTitle': 'office-profile',
        'title': 'create-office-phone-number',
        'form': form,
    }
    return render(request, 'office/createOfficePhoneNumber.html', context)


# تعديل رقم هاتف القسم
@login_required(login_url='account:logout')
def phoneNumberUpdate(request, phone_number_id):
    if request.user.user_type != is_office:
        return redirect('account:logout')

    data = get_object_or_404(TblOfficePhone, pk=phone_number_id, office=request.user.pk)
    form = PhoneNumberForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST or None, request.FILES or None, instance=data)
        if form.is_valid():
            fd = form.save(commit=False)
            fd.save()
            return redirect('office:office-profile')
    context = {
        'parentTitle': 'office-profile',
        'title': 'phone-number-update',
        'form': form,
    }
    return render(request, 'office/phoneNumberUpdate.html', context)


# حذف رقم هاتف القسم
@login_required(login_url='account:logout')
def phoneNumberDelete(request, phone_number_id):
    if request.user.user_type != is_office:
        return redirect('account:logout')

    phone = get_object_or_404(TblOfficePhone, pk=phone_number_id, office=request.user.pk)
    if request.method == 'POST':
        phone.delete()
        return redirect("office:office-profile")
    context = {
        'parentTitle': 'office-profile',
        'title': 'phone-number-delete',
        'phone': phone,
    }
    return render(request, 'office/phoneNumberDelete.html', context)

from django.db.models import Sum


from datetime import datetime

# احصائيات المكتب
@login_required(login_url='account:logout')
def officeStatistics(request):
    if request.user.user_type != is_office:
        return redirect('account:logout')
    
    if request.method == 'GET':
        start = request.GET.get('start')
        end = request.GET.get('end')
        if start is not None:
            start = start
        else:
            start = ''
        if end is not None:
            end = end
        else:
            end = ''
        if start == '' and end == '':
            outgoing_transfers = TblMoneyTransfer.objects.filter(sender_office=request.user.pk)
            incoming_transfers = TblMoneyTransfer.objects.filter(recipient_office=request.user.pk)
        if start != '' and end != '':
            outgoing_transfers = TblMoneyTransfer.objects.filter(sender_office=request.user.pk, sent_at__date__gte=start, sent_at__date__lte=end)
            incoming_transfers = TblMoneyTransfer.objects.filter(recipient_office=request.user.pk, sent_at__date__gte=start, sent_at__date__lte=end)
        elif start != '':
            print('===[1]===')
            outgoing_transfers = TblMoneyTransfer.objects.filter(sender_office=request.user.pk, sent_at__date=start)
            incoming_transfers = TblMoneyTransfer.objects.filter(recipient_office=request.user.pk, sent_at__date=start)
        elif end != '':
            print('===[1]===')
            outgoing_transfers = TblMoneyTransfer.objects.filter(sender_office=request.user.pk, sent_at__date=end)
            incoming_transfers = TblMoneyTransfer.objects.filter(recipient_office=request.user.pk, sent_at__date=end)


    '''
    # الحوالات 
    '''

    outgoing_transfers_count = outgoing_transfers.count()
    incoming_transfers_count = incoming_transfers.count()
    '''
    # الموافق عليها
    '''
    done_outgoing_transfers = outgoing_transfers.filter(approval_by_recipient=True, rejection=False)
    # اجمالي الحوالات المرسلة
    done_outgoing_transfers_count = done_outgoing_transfers.count()
    # اجمالي المبلغ المرسل
    sent_amount = done_outgoing_transfers.aggregate(Sum('sent_amount'))
    if sent_amount['sent_amount__sum'] == None:
        sent_amount_count = 0
    else:
        sent_amount_count = sent_amount['sent_amount__sum']
    # اجمالي عمولة المرسل
    sender_commission = done_outgoing_transfers.aggregate(Sum('sender_commission'))
    if sender_commission['sender_commission__sum'] == None:
        sender_commission_count = 0
    else:
        sender_commission_count = sender_commission['sender_commission__sum']
    # اجمالي العمولة المأخوذة من المرسل 
    commission_from_sender = done_outgoing_transfers.aggregate(Sum('commission_from_sender'))
    if commission_from_sender['commission_from_sender__sum'] == None:
        commission_from_sender_count = 0
    else:
        commission_from_sender_count = commission_from_sender['commission_from_sender__sum']
    # اجمالي ربح المرسل
    gross_profit = sender_commission_count - commission_from_sender_count
    # ===========================
    # الحوالات الواردة
    done_incoming_transfers = incoming_transfers.filter(approval_by_recipient=True, rejection=False)
    # اجمالي الحوالات الواردة
    done_incoming_transfers_count = done_incoming_transfers.count()
    # اجمالي المبلغ الوارد
    incoming_sent_amount = done_incoming_transfers.aggregate(Sum('sent_amount'))
    if incoming_sent_amount['sent_amount__sum'] == None:
        incoming_sent_amount_count = 0
    else:
        incoming_sent_amount_count = incoming_sent_amount['sent_amount__sum']
    # اجمالي عمولة المستقبل
    recipient_commission = done_incoming_transfers.aggregate(Sum('recipient_commission'))
    if recipient_commission['recipient_commission__sum'] == None:
        recipient_commission_count = 0
    else:
        recipient_commission_count = recipient_commission['recipient_commission__sum']
    # اجمالي العمولة المأخوذة من المستلم 
    commission_from_recipient = done_incoming_transfers.aggregate(Sum('commission_from_recipient'))
    if commission_from_recipient['commission_from_recipient__sum'] == None:
        commission_from_recipient_count = 0
    else:
        commission_from_recipient_count = commission_from_recipient['commission_from_recipient__sum']
    # اجمالي ربح المستلم
    incoming_gross_profit = recipient_commission_count - commission_from_recipient_count
    '''
    # المعلقة
    '''
    waiting_outgoing_transfers = outgoing_transfers.filter(approval_by_recipient=False, rejection=False)
    waiting_outgoing_transfers_count = waiting_outgoing_transfers.count()
    waiting_incoming_transfers = incoming_transfers.filter(approval_by_recipient=False, rejection=False)
    waiting_incoming_transfers_count = waiting_incoming_transfers.count()
    '''
    # المرفوضة
    '''
    rejected_outgoing_transfers = outgoing_transfers.filter(rejection=True, approval_by_recipient=False)
    rejected_outgoing_transfers_count = rejected_outgoing_transfers.count()
    rejected_incoming_transfers = incoming_transfers.filter(recipient_office=request.user.pk, rejection=True, approval_by_recipient=False)
    rejected_incoming_transfers_count = rejected_incoming_transfers.count()

    context = {
        'title': 'office-statistics',
        'start': start, 'end': end,
        # =========================================================================
        'outgoing_transfers_count': outgoing_transfers_count,
        'done_outgoing_transfers_count': done_outgoing_transfers_count,
        'sent_amount_count': sent_amount_count,
        'sender_commission_count': sender_commission_count,
        'commission_from_sender_count': commission_from_sender_count,
        'gross_profit': gross_profit,
        'waiting_outgoing_transfers_count': waiting_outgoing_transfers_count,
        'rejected_outgoing_transfers_count': rejected_outgoing_transfers_count,
        # =========================================================================
        'incoming_transfers_count': incoming_transfers_count,
        'done_incoming_transfers_count': done_incoming_transfers_count,
        'incoming_sent_amount_count': incoming_sent_amount_count,
        'recipient_commission_count': recipient_commission_count,
        'commission_from_recipient_count': commission_from_recipient_count,
        'incoming_gross_profit': incoming_gross_profit,
        'waiting_incoming_transfers_count': waiting_incoming_transfers_count,
        'rejected_incoming_transfers_count': rejected_incoming_transfers_count,
        # =========================================================================
        'transfers_count': outgoing_transfers_count+incoming_transfers_count,
        'done_transfers_count': done_outgoing_transfers_count+done_incoming_transfers_count,
        'waiting_transfers_count': waiting_outgoing_transfers_count+waiting_incoming_transfers_count,
        'rejected_transfers_count': rejected_outgoing_transfers_count+rejected_incoming_transfers_count,
        'amount_count': sent_amount_count+incoming_sent_amount_count,
        'commission_count': sender_commission_count+recipient_commission_count,
        'commission_from_office_count': commission_from_sender_count+commission_from_recipient_count,
        'gross_profit_count': gross_profit+incoming_gross_profit,
    }
    return render(request, 'office/officeStatistics.html', context)





