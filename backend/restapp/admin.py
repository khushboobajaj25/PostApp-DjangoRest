from django.contrib import admin
from restapp import models
# Register your models here.


@admin.register(models.Post)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'updated_at']
    list_filter = ('created_at','updated_at')
