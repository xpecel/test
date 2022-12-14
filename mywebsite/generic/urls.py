from django.urls import path
from . views import  index, test_speed, weather

urlpatterns = [
    path('', index, name='index'),
    path('weather/', weather, name='weather'),
    path('speedtes/<int>', test_speed)
]
