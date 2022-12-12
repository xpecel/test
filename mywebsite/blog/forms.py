from django.forms import ModelForms
from django import forms

class BlogForm(ModelForms):
    class Meta:
        fields = '`'
