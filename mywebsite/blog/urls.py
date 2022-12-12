from django.urls import path, re_path
from .views import  postingan, semua_postingan, kategori
urlpatterns = [
        path('', semua_postingan, name='semua_postingan'),
        path('kategori/<category>/', kategori, name='kategori'),
        #re_path(r'^(?P<tahun>[0-9]{4})/(?P<bulan>[0-9]{2})/(?P<hari>[0-9]{2})/', tahun, name='tahun'),
        path('post/<slug>/', postingan, name='postingan'),
]

