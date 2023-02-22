from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from account.models import TblUser
from .models import TblMoneyTransfer, TblOfficePhone
from account.models import TblOfficeUser, CITY_CHOICES

class OfficeProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(label='اسم المكتب', required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control mt-1',
        'placeholder': 'ادخل اسم المكتب'
    }))
    email = forms.EmailField(label='البريد الالكتروني', required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control mt-1',
        'placeholder': 'ادخل البريد الالكتروني'
    }))
    address = forms.CharField(label='العنوان', required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control mt-1',
        'placeholder': 'ادخل العنوان'
    }))
    city = forms.ChoiceField(label='المدينة', required=True, choices=CITY_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control mt-1'
    }))
    url_address = forms.CharField(label='العنوان على خارطة قوقل', required=True, max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control mt-1',
        'placeholder': 'ادخل العنوان على خارطة قوقل'
    }))
    bio = forms.CharField(label='نبذة تعريفية', required=False, max_length=1500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'أدخل نص النبذة التعريفية...',
        'rows': '3',
    }))
    class Meta:
        model = TblOfficeUser
        fields = ('name', 'bio', 'email', 'city', 'address', 'url_address')


class CreateMoneyTransferForm(forms.ModelForm):
    sent_amount = forms.FloatField(label='المبلغ المرسل', required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل المبلغ المرسل'
    }))
    sender_commission = forms.FloatField(label='عمولة المرسل', required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل عمولة المرسل'
    }))
    recipient_commission = forms.FloatField(label='عمولة المستقبل', required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل عمولة المستقبل'
    }))
    note = forms.CharField(label='ملاحظه', required=False, max_length=200, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'أدخل نص الملاحظه...',
        'rows': '3',
    }))
    class Meta:
        model = TblMoneyTransfer
        fields = ('sent_amount', 'sender_commission', 'recipient_commission', 'note')


class ApprovalMoneyTransferForm(forms.ModelForm):
    approval_by_recipient = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
    }))
    note2 = forms.CharField(label='ملاحظة', required=False, max_length=250, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'أدخل نص الملاحظه...',
        'rows': '3',
    }))
    class Meta:
        model = TblMoneyTransfer
        fields = ('approval_by_recipient', 'note2')


class RejectionMoneyTransferForm(forms.ModelForm):
    rejection = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
    }))
    note2 = forms.CharField(label='ملاحظة سبب رفض الحوالة', required=False, max_length=250, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'أدخل نص الملاحظه...',
        'rows': '3',
    }))
    class Meta:
        model = TblMoneyTransfer
        fields = ('rejection', 'note2')


class MoneyTransferForm(forms.ModelForm):
    class Meta:
        model = TblMoneyTransfer
        fields = ('sender_office', 'recipient_office', 'sent_amount', 'sender_commission', 
        'recipient_commission', 'commission_from_sender', 'commission_from_recipient', 'note')


class ChangeOfficePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='كلمة المرور القديمة', max_length=100, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'ادخل كلمة المرور القديمة'
    }))
    new_password1 = forms.CharField(label='كلمة المرور الجديدة', max_length=100, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'ادخل كلمة المرور الجديدة'
    }))
    new_password2 = forms.CharField(label='تأكيد كلمة المرور الجديدة', max_length=100, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'ادخل كلمة المرور الجديدة'
    }))
    class Meta:
        model = TblUser
        fields = ('old_password', 'new_password1', 'new_password2')


class PhoneNumberForm(forms.ModelForm):
    phone = forms.CharField(label='رقم الهاتف', required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل رقم الهاتف'
    }))
    class Meta:
        model = TblOfficePhone
        fields = ('phone', )


