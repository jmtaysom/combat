import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Firefox()
    driver.get('http://localhost:8000')
    yield driver
    print('tearing down browser')
    driver.quit()

def test_title(browser):
    assert 'Combat' in browser.title



