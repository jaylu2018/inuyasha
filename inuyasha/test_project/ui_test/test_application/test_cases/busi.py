from inuyasha import TestCase


class TestSample(TestCase):

    def test_web_case(self, playwright):
        page = self.page(playwright, name="chrome")
        page.goto("https://www.baidu.com")
