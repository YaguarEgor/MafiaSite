from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomPlayerCreationForm, CustomPlayerChangeForm





class CustomPlayerAdmin(UserAdmin):
    add_form = CustomPlayerCreationForm
    form = CustomPlayerChangeForm
    model = CustomPlayer
    list_display = ['email', 'username',]

admin.site.register(CustomPlayer, CustomPlayerAdmin)
