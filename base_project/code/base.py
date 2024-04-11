from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.driver_finder import logger
from selenium.webdriver.support import expected_conditions as ec
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from setuptools.command import alias

from ui.locators import locators


CLICK_RETRY = 3


class BaseCase:
    driver = None
    wait = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(locator))
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator)
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def login(self):
        email = 'svet.kai096@gmail.com'
        password = 'ghhsdh1456'

        try:
            self.click(locators.HEAD_LOGIN_BUTTON_LOCATOR)
            self.paste(locators.INPUT_EMAIL_LOCATOR, email)
            self.paste(locators.INPUT_PASSWORD_LOCATOR, password)
            self.click(locators.AUTH_LOGIN_BUTTON_LOCATOR)
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locators.CHECK_PAGE_LOADED_LOCATOR))
        except (TimeoutException, StaleElementReferenceException):
            logger.error(
                f"Произошла TimeoutException или StaleElementReferenceException. Элемент не найден: {alias}"
            )
            return None

    def logout(self):
        self.login()

        try:
            self.click(locators.MODULE_BUTTON_LOCATOR)
            logout_button = self.find(locators.LOGOUT_BUTTON_FIELD_LOCATOR)
            ActionChains(self.driver).move_to_element(logout_button).click().perform()
        except (TimeoutException, StaleElementReferenceException):
            logger.error(
                f"Произошла TimeoutException или StaleElementReferenceException. Элемент не найден: {alias}"
            )
            return None

    def edit(self):
        full_name = 'Кайсина Светлана Дмитриевна'
        inn = '827347428101'
        phone_number = '+78005553535'

        self.login()
        try:
            profile_button = self.find(locators.PROFILE_BUTTON_LOCATOR)
            ActionChains(self.driver).move_to_element(profile_button).click().perform()
            self.paste(locators.FIO_FIELD_LOCATOR, full_name)
            self.paste(locators.INN_FIELD_LOCATOR, inn)
            self.paste(locators.PHONE_NUMBER_FIELD_LOCATOR, phone_number)
            self.click(locators.SUBMIT_EDIT_BUTTON_LOCATOR)
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(locators.SUCCESS_SAVE_LOCATOR))
        except (TimeoutException, StaleElementReferenceException):
            logger.error(
                f"Произошла TimeoutException или StaleElementReferenceException. Элемент не найден: {alias}"
            )
            return None

    def page_change(self, locator, url, obj_locator):
        self.login()
        try:
            self.click(locator)
            assert self.driver.current_url == url
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(obj_locator))
        except (TimeoutException, StaleElementReferenceException):
            logger.error(
                f"Произошла TimeoutException или StaleElementReferenceException. Элемент не найден: {alias}"
            )
            return None

    def clear_field(self, locator):
            self.find(locator).send_keys(Keys.CONTROL + "a")
            self.find(locator).send_keys(Keys.DELETE)

    def paste(self, locator, info):
        try:
            self.clear_field(locator)
            self.find(locator).send_keys(info)
        except (TimeoutException, StaleElementReferenceException):
            logger.error(
                f"Произошла TimeoutException или StaleElementReferenceException. Элемент не найден: {alias}"
            )
            return None



