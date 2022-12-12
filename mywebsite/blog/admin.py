from django.contrib import admin
from . models import Post
# Register your models here.
class Filtering(admin.ModelAdmin):
    list_display = ['id', 'judul',  'category', 'dibuat' ]
    readonly_fields = ['slug']

admin.site.register(Post, Filtering)
