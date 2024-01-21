from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields='__all__'
        
        