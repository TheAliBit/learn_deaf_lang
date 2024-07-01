from django.contrib import admin
from django.utils.text import slugify
from . import models


class WordAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Category)
admin.site.register(models.Word, WordAdmin)
