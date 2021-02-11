from rest_framework import serializers
from .models import *


class NewsSerializers(serializers.ModelSerializer):
    """
    Сериализация модели News.
    """
    class Meta:
        model = News
        fields = '__all__'
