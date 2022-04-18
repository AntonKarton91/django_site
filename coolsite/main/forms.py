from django import forms
from .models import *

class RegistrationForm(forms.Form):
    name=forms.CharField(max_length=10, label='Имя', widget=forms.TextInput(attrs={'class':'form-input'}))
    surname=forms.CharField(max_length=10, label='Фамилия', widget=forms.TextInput(attrs={'class':'form-input'}))
    position=forms.ModelChoiceField(queryset=Positions.objects.all(), label='Должность',
                                    empty_label='нет')

