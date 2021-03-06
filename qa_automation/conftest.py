import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()