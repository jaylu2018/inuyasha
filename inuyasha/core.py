import os

from inuyasha.driver.api import BaseRequest
from inuyasha.driver.web import BasePage
from inuyasha.config import inuyasha_str


class TestCase:

    @classmethod
    def setup_class(cls):
        print(inuyasha_str)
        print('------------------------------用例测试启动🚀🚀🚀------------------------------')
        cls.api()

    @staticmethod
    def page(play: object, name: str = None):
        print('首次运行会下载浏览器驱动⏬，请耐心等待⌛️')
        os.system('python -m playwright install')
        return BasePage(play, name=name)

    @classmethod
    def api(cls):
        cls.requests = BaseRequest
