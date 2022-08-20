from django.contrib import admin

from News.models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass