from django import forms
from django.forms import fields, widgets

from rooms.models import Rooms

class RoomForm(forms.Form):
    class Meta:
        model = Rooms
        fields = ['name']