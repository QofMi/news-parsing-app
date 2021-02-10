from django.contrib import admin
from .models import News


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    """
    Регистраци модели AdminNews в административной части сайта
    """
    list_display = ['title', 'url', 'created']
