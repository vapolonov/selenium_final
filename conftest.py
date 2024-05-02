import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--language', action='store', default='en', help='Choose language: en or ru'
    )


@pytest.fixture
def get_link(request):
    language = request.config.getoption("language")
    if language != 'en':
        raise ValueError("Invalid language choice")
    url = f"http://selenium1py.pythonanywhere.com/{language}-gb"
    return url


@pytest.fixture
def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser..')
    browser.quit()
