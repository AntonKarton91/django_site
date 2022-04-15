from django import forms
from .models import *

class RegistrationForm(forms.Form):
    name=forms.CharField(max_length=10, label='Имя')
    surname=forms.CharField(max_length=10, label='Фамилия')
    position=forms.ModelChoiceField(queryset=Positions.objects.all(), label='Должность')

