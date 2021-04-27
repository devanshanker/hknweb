from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question

# Registering Question model.
admin.site.register(Question)
