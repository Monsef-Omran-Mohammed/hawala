from django import forms
from account.models import TblUser, TblOfficeUser


class OfficeEmailUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='البريد الالكتروني (خاص)', required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control mt-1',
        'placeholder': 'ادخل البريد الالكتروني'
    }))
    class Meta:
        model = TblUser
        fields = ('email', )

class OfficePhoneUpdateForm(forms.ModelForm):
    special_phone = forms.CharField(label='رقم الهاتف (خاص)', required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'ادخل رقم الهاتف'
    }))
    class Meta:
        model = TblUser
        fields = ('special_phone', )


class OfficeActiveUpdateForm(forms.ModelForm):
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
    }))
    class Meta:
        model = TblUser
        fields = ('is_active', )
