from django import forms
from django.forms import ModelForm, fields
from .models import *

class Taskform(forms.ModelForm):
    
    
    class  Meta:
        model=Task
        fields='__all__'