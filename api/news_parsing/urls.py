from django.urls import path
from .views import *


urlpatterns = [
    path('posts', GetNews.as_view())
]
