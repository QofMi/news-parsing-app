import requests
from .test_setup import TestSetUp


API_URL = 'http://localhost:5000/posts'


class TestNews(TestSetUp):

    def test_get_news(self):
        req = requests.get(API_URL)
        assert req.status_code == 200

    def test_news_post(self):
        req = requests.post(API_URL)
        assert req.status_code == 200

    def test_get_news_after_created_news(self):
        req = requests.get(API_URL)
        assert req.status_code == 200

    def test_get_news_with_order(self):
        req = requests.get(API_URL + '?order=created')
        assert req.status_code == 200

    def test_get_news_with_order_bad(self):
        req = requests.get(API_URL + '?order=invalid_attribute')
        assert req.status_code == 400

    def test_get_news_with_offset_and_limit(self):
        req = requests.get(API_URL + '?offset=0&limit=10')
        assert req.status_code == 200

    def test_get_news_with_offset_and_limit_bad(self):
        req = requests.get(API_URL + '?offset=0&limit=-6')
        assert req.status_code == 400

    def test_get_news_with_all(self):
        req = requests.get(API_URL + '?order=-title&offset=0&limit=10')
        assert req.status_code == 200

    def test_get_news_with_all_bad(self):
        req = requests.get(API_URL + '?order=invalid_attribute&offset=-1&limit=-5')
        assert req.status_code == 400
