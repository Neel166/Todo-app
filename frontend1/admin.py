from django.contrib import admin
from .models import Frontend1

class Frontend1Admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

admin.site.register(Frontend1, Frontend1Admin)