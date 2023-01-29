from django import forms
from django.forms import fields, widgets

from rooms.models import Rooms

class RoomForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Rooms
        fields = ['name']