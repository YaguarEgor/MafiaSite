from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomPlayer

class CustomPlayerCreationForm(UserCreationForm):

    class Meta:
        model = CustomPlayer
        fields = ('username', 'email')

class CustomPlayerChangeForm(UserChangeForm):

    class Meta:
        model = CustomPlayer
        fields = ('username', 'email')