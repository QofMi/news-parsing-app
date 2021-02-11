import logging
import validators
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from django.http import Http404
from .utils import *


ORDER_QUERY_PARAMS = ['title', '-title', 'url', '-url', 'created', '-created']


class GetNewsMixin:
    model = None
    serializer = None
    default_limit = None

    def get(self, request):
        """
        Получение списка постов с возможностью фильтрации.
        """
        try:
            object = self.model.objects.all()[0:int(self.default_limit)]

            order = request.query_params.get('order', '')
            offset = request.GET.get('offset', '')
            limit = request.query_params.get('limit', '')

            if order:
                if not order in ORDER_QUERY_PARAMS:
                    raise Exception('Invalid order')
            if offset or limit:
                if int(offset) < 0:
                    raise Exception('Invalid offset')
                if int(offset) > self.model.objects.all().count():
                    raise Exception('Invalid offset')
                if int(limit) < 0:
                    raise Exception('Invalid limit')

            if offset and limit:
                object = self.model.objects.all()[int(offset):int(offset)+int(limit)]

            for i in range(0, len(ORDER_QUERY_PARAMS)):
                if order == ORDER_QUERY_PARAMS[i]:
                    object = self.model.objects.all().order_by(ORDER_QUERY_PARAMS[i])[0:int(self.default_limit)]
                if order == ORDER_QUERY_PARAMS[i] and offset and limit:
                    object = self.model.objects.all().order_by(ORDER_QUERY_PARAMS[i])[int(offset):int(offset)+int(limit)]

            serializer = self.serializer(object, many=True).data
            return Response(serializer)
        except Exception as error:
            logging.error(f"ERROR -------> {error}")
            raise ParseError(error)

    def post(self, request):
        """
        Создание новостных постов.
        """
        try:
            serializer = self.serializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                get_news()
                for i in range(0, len(NEWS)):
                    title = NEWS[i].split('**')[0]
                    url = NEWS[i].split('**')[-1]
                    object = self.model.objects.filter(url=url)

                    if validators.url(url):
                        new_object = self.model(
                            title=title,
                            url=url
                        )
                        if not object:
                            new_object.save()
                NEWS.clear()
                return Response('Accepted')
        except Exception as error:
            logging.error(f"ERROR -------> {error}")
            raise ParseError(error)
