import pytest
import sys
import os
from pages.main_page import MainPage

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_guest_can_go_to_login_page(browser, request):
    lang = request.config.getoption('language')
    if lang == "en":
        link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    elif lang == 'ru':
        link = 'http://selenium1py.pythonanywhere.com/ru/'
    else:
        raise pytest.UsageError('--language should be en or ru')
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

