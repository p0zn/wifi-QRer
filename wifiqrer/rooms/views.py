from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from rooms.forms import RoomForm
from rooms.models import Rooms 


def index(request):
    
    wifi_form = RoomForm(request.POST or None)

    context = {
        "wifi_form" : wifi_form,
    }     
    if request.method == 'POST':
        if wifi_form.is_valid():
            name = wifi_form.cleaned_data['name']
            password = wifi_form.cleaned_data['password']
            wifi_qr = Rooms.objects.create(name = name , password = password)
            print(wifi_qr)
            wifi_qr.save() 
            return HttpResponseRedirect(reverse('wifi_qr_detail', args=[wifi_qr.id]))
    return render(request,'rooms/index.html',context)


def wifi_qr_detail(request,id):
    user_qr = Rooms.objects.filter(id = id).first()

    context = {
        "user_qr" : user_qr,
    }
    return render(request,"rooms/qr_detail.html",context)