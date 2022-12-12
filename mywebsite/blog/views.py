from django.shortcuts import render
from . models import Post
import os
import datetime
# Create your views here.

# tampilkan semua postingan
def semua_postingan(request):
    post = Post.objects.all()
    return render(request, 'semua-postingan.html', {'post':post, 'judul':'Semua postingan'})

# mensortir berdasarkan kategori
def kategori(request, category):
    os.system('clear')
    kategori = category
    post = Post.objects.filter(category__iexact=kategori)
    semua_kategori = Post.objects.values('category').distinct()
    konteks = {
            'title':'Home',
            'heading':f'Selamat datang {kategori.capitalize()}',
            'post' : post,
            'kategori':kategori,
            'semua_kategori':semua_kategori,
            }
    return render(request, 'home.html', konteks)

# tampilkan field
def postingan(request, slug):
    post = Post.objects.get(slug=slug)
    print('berhasil')
    return render(request, 'postingan.html', {'post':post}) 

