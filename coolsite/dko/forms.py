import form as form
from django import forms

from dko import models
from .models import *

# class AddTask(models.Model):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model=Tasks
#         fields='__all__'
#         widgets={
#             'numder':forms.TextInput(attrs={'class':'label'})
#         }

class AddEmployer(forms.ModelForm):
    class Meta:
        model = MarketEmployer
        fields = ['name', 'surname','status']
