import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb")


@pytest.fixture(scope="function")
def user_language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nStart browser...")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser")
    browser.quit()
