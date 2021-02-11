from apscheduler.schedulers.background import BackgroundScheduler
from news_parsing.models import *
import logging
import validators
from news_parsing.utils import *


def update_news():
    """
    Обновление новостей.
    """
    try:
        get_news()
        for i in range(0, len(NEWS)):
            title = NEWS[i].split('**')[0]
            url = NEWS[i].split('**')[-1]
            object = News.objects.filter(url=url)

            if validators.url(url):
                new_object = News(
                    title=title,
                    url=url
                )
                if not object:
                    new_object.save()
        NEWS.clear()
    except Exception as error:
        logging.error(f"ERROR -------> {error}")


def start():
    """
    Планировщик
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_news, "interval" ,minutes=1, id="1", replace_existing=True)
    scheduler.start()
