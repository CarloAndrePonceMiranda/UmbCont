# This Python file uses the following encoding: utf-8
from django import forms
from django.forms import EmailInput, TextInput
from .models import Playera

class UmbrellaForm(forms.ModelForm):
    class Meta:
        model = Playera
        fields = '__all__'
