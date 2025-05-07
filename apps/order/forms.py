from django import forms
from .models import Order
from phonenumber_field.formfields import PhoneNumberField

class OrderForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        label='Telefon raqami',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+998 XX XXX XX XX'})
    )
    date = forms.DateField(
        label='Sana',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    person = forms.IntegerField(
        label='Kattalar soni',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '1'})
    )
    child = forms.IntegerField(
        label='Bolalar soni',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0'})
    )

    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'tour', 'date', 'person', 'child']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'tour': forms.Select(attrs={'class': 'form-select'}),
        }