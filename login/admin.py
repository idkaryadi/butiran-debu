from django.contrib import admin
from .models import Login

# Register your models here.
my_model = Login
admin.site.register(my_model)