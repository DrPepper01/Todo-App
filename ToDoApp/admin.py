from django.contrib import admin
from .models import Category, ToDo
# Register your models here.

admin.site.register(ToDo)
admin.site.register(Category)