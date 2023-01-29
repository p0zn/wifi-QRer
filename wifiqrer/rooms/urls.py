from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('qr_detail/<int:id>', views.wifi_qr_detail, name="wifi_qr_detail"),
   
]

