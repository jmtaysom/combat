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
    header_text = browser.find_element_by_tag_name('h3').text
    assert 'Initiative' in header_text
    table = browser.find_element_by_tag_name('table').text
    assert 'Initiative' in table

