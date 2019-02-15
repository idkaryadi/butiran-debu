from django.contrib import admin
from .models import Home, Kategori

# Register your models here.
my_model = [Home, Kategori]
admin.site.register(my_model)