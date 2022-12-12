from django.db import models
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    judul = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    category = models.CharField(max_length=255)
    dibuat = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(null=True, blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.judul)
        super(Post, self).save()
    def __str__(self):
        return f'{self.id}. {self.judul}'
