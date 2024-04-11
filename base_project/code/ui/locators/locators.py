from selenium.webdriver.common.by import By


MAIN_PAGE_LOADED_LOCATOR = (By.XPATH, '//*[contains(@class, "mainPage-module-button")]')

HEAD_LOGIN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
INPUT_EMAIL_LOCATOR = (By.NAME, 'email')
INPUT_PASSWORD_LOCATOR = (By.NAME, 'password')
AUTH_LOGIN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
CHECK_PAGE_LOADED_LOCATOR = (By.XPATH, '//div[contains(@class, "instruction-module-title")]')

MODULE_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
LOGOUT_BUTTON_FIELD_LOCATOR = (By.XPATH, '//a[@href="/logout" and contains(@class, "rightMenu-module-rightMenuLink")]')

PROFILE_BUTTON_LOCATOR = (By.XPATH, '//a[contains(@class, "center-module-profile")]')
FIO_FIELD_LOCATOR = (By.XPATH, '//*[@data-name="fio"]//input')
INN_FIELD_LOCATOR = (By.XPATH, '//*[@data-name="ordInn"]//input')
PHONE_NUMBER_FIELD_LOCATOR = (By.XPATH, '//*[@data-name="phone"]//input')
SUBMIT_EDIT_BUTTON_LOCATOR = (By.XPATH, '//button[contains(@class, "button_submit") and @data-class-name="Submit"]')
SUCCESS_SAVE_LOCATOR = (By.XPATH, '//div[contains(@class, "_notification _notification_success")]')

BILLING_BUTTON_LOCATOR = (By.XPATH, '//a[contains(@class, "center-module-billing")]')
BILLING_PAGE_LOADED_LOCATOR = (By.XPATH, '//div[contains(@class, "deposit__payment-form-wrapper")]')
PRO_BUTTON_LOCATOR = (By.XPATH, '//a[contains(@class, "center-module-pro") and @href="/pro"]')
PRO_PAGE_LOADED_LOCATOR = (By.XPATH, '//div[contains(@class, "t_col_first_big")]')
