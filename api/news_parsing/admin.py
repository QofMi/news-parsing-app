from django.contrib import admin
from .models import News


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    """
    Регистраци модели News в административной панели.
    """
    list_display = ['title', 'url', 'created']
