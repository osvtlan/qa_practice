import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from ui.locators import locators


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'none'
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.get('https://target.my.com')
    WebDriverWait(browser, 5).until(ec.presence_of_element_located(locators.MAIN_PAGE_LOADED_LOCATOR))
    yield browser
    browser.quit()

