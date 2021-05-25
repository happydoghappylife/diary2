from django import forms
from django.db.models import fields
from .models import Mydiary

class MydiaryForm(forms.ModelForm):
    class Meta: 
        model = Mydiary
        fields = ['title', 'body','image']
