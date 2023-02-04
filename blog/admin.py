from django.contrib import admin
# from django import forms
# from ckeditor.widgets import CKEditorWidget


# Register your models here.

from .models import Blog
from .models import Category


admin.site.register(Blog)
admin.site.register(Category)
