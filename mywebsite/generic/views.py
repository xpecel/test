from django.shortcuts import HttpResponse, HttpResponseRedirect, redirect, render
import os
from background_task import background
# Create your views here.

def index(request):
    os.system('clear')
    if request.user_agent.browser.family == 'curl':
        return HttpResponse('i\'m alive!')
    else:
        space_landed = os.popen('cat templates/space.txt')
        konteks = {
            'space_landed':space_landed.read(),
            'title':'~'
        }
        return render(request, 'index.html', konteks )

kota = ''
def hapus():
    a = os.system('tree media/')
    print(a, kota)
    os.system(f'clear; pwd ; rm media/image/weather/{kota}*.png;')
def weather(request):
    if request.POST:
        kota = request.POST['kota'].replace(' ','')
        cuaca = os.popen(f'curl id.wttr.in/{kota}?format="%l:+%c+%t+%C"')
        os.system(f'wget wttr.in/{kota}_0tqp_lang=id.png -P media/image/weather/')
        gambar_location = f'../media/image/weather/{kota}_0tqp_lang=id.png'
        konteks = {
            'cuaca':cuaca.read(),
            'title':cuaca.read(),
            'gambar':gambar_location,
        }
        hapus()
        return render(request, 'weather.html', konteks)

    else:
        return render(request, 'weather.html', {'title':'Weather'})


def test_speed(request, jumlah):
    ekse = ''
    for jumlah in jumlah
        ekse += ' speedtest; '
    os.system(f'{ekse}')
    selesai = f'speedtest sebanya {jumlah} selesai!'
    return HttpResponse(selesai)

