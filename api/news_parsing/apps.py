from django.apps import AppConfig


class NewsParsingConfig(AppConfig):
    name = 'news_parsing'
    verbose_name = 'Новости'

    def ready(self):
        from .news_scheduler import news_updater
        news_updater.start()
