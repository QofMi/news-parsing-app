from rest_framework.views import APIView
from .models import *
from .serializers import *
from .services import *


class GetNews(GetNewsMixin, APIView):
    """
    Получение списка постов с возможностью фильтрации.
    Создание новостных постов.
    """
    model = News
    serializer = NewsSerializers
    default_limit = 5
