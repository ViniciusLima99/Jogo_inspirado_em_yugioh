from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .model import Player

class PlayerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form_control'
            
    class Meta:
        model = Player
        fields = 'username',
        
class BotaoForm(forms.Form):
    botao_id = forms.CharField()
    
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
            super(UserForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form_control'
    class Meta:
        model = User
        fields = ['username', 'password']  # Inclua os campos que deseja

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash da senha
        if commit:
            user.save()
        return user