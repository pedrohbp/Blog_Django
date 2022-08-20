from django.contrib import admin

from Category.models import Category

@admin.register(Category)
class NewsAdmin(admin.ModelAdmin):
    pass