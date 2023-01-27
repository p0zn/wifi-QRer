from django.shortcuts import render

from rooms.forms import RoomForm


def index(request):
    return render(request,'rooms/index.html')
