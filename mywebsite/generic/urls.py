from django.urls import path
from . views import  check_bandwith, index, speedtest, weather

urlpatterns = [
    path('', index, name='index'),
    path('weather/', weather, name='weather'),
    path('speedtest/<int:jumlah>/', speedtest),
    path('usage/', check_bandwith),
]
