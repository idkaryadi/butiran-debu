from __future__ import unicode_literals

from django.contrib import admin
from .models import Reserv
# Register your models here.

my_model = [Reserv]
admin.site.register(my_model)

# -*- coding: utf-8 -*-

# Register your models here.

from .models import Review

my_model = [Review]
admin.site.register(my_model)
