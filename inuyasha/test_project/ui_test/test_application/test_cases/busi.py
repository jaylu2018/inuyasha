from inuyasha import TestCase
from inuyasha.test_project.ui_test.test_application.page_objects.login import Login


class TestLogin(TestCase):

    def test_login(self, playwright):
        page = self.page(playwright, name="chrome")
        Login().login(page)
