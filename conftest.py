import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: en or ru')


@pytest.fixture(scope="function")
def browser(request):
    print('\nstart browser for test..')
    lang = request.config.getoption('language')
    if lang == "en":
        link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    elif lang == 'ru':
        link = 'http://selenium1py.pythonanywhere.com/ru/'
    else:
        raise pytest.UsageError('--language should be en or ru')
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    print('\nquit browser..')
    browser.quit()
