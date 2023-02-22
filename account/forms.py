from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *



class OfficeSignUpForm(UserCreationForm):
    username = forms.CharField(label='اسم المستخدم (معرف الحساب)', required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'autofocus': "false",
        'placeholder': 'ادخل اسم المستخدم'
    }))
    email = forms.EmailField(label='البريد الالكتروني (خاص)', required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل البريد الالكتروني'
    }))
    password1 = forms.CharField(label='كلمة المرور', max_length=100, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'ادخل كلمة المرور'
    }))
    password2 = forms.CharField(label='تأكيد كلمة المرور', max_length=100, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'ادخل كلمة المرور'
    }))
    name = forms.CharField(label='اسم المكتب', required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل اسم المكتب'
    }))
    public_email = forms.EmailField(label='البريد الالكتروني (عام)', required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل البريد الالكتروني'
    }))
    special_phone = forms.CharField(label='رقم الهاتف (خاص)', required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل رقم الهاتف'
    }))
    city = forms.ChoiceField(label='المدينة', required=True, choices=CITY_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    address = forms.CharField(label='العنوان', required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل العنوان'
    }))
    url_address = forms.CharField(label='العنوان على خارطة قوقل', required=True, max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل العنوان على خارطة قوقل'
    }))
    bio = forms.CharField(label='نبذة تعريفية', required=False, max_length=1500, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'أدخل نص النبذة التعريفية...',
        'rows': '3',
    }))

    class Meta(UserCreationForm.Meta):
        model = TblUser
        fields = (
            'username', 'email', 'password1', 'password2'
        )
        extra_kwargs = { 'email': {'required': True} }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.is_staff = True
        user.save()
        office = TblOfficeUser.objects.create(user=user)
        office.name = self.cleaned_data.get('name')
        office.email = self.cleaned_data.get('public_email')
        office.special_phone = self.cleaned_data.get('special_phone')
        office.city = self.cleaned_data.get('city')
        office.address = self.cleaned_data.get('address')
        office.url_address = self.cleaned_data.get('url_address')
        office.bio = self.cleaned_data.get('bio')
        office.save()
        return user




class OfficeUserForm(forms.ModelForm):
    class Meta:
        model = TblOfficeUser
        fields = '__all__'