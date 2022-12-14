from django.urls import path
from . views import  index, speedtest, weather

urlpatterns = [
    path('', index, name='index'),
    path('weather/', weather, name='weather'),
    path('speedtest/<int:jumlah>/', speedtest)
]
