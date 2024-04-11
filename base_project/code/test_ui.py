from base import BaseCase
from ui.locators import locators
import pytest


class TestUI(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login()

    @pytest.mark.UI
    def test_logout(self):
        self.logout()

    @pytest.mark.UI
    def test_edit_info(self):
        self.edit()

    @pytest.mark.parametrize(
        'locator, url, obj_locator',
        [
            (
                locators.BILLING_BUTTON_LOCATOR,
                'https://target.my.com/billing',
                locators.BILLING_PAGE_LOADED_LOCATOR,
            ),
            (
                locators.PRO_BUTTON_LOCATOR,
                'https://target.my.com/pro',
                locators.PRO_PAGE_LOADED_LOCATOR,
            ),
        ],
    )
    @pytest.mark.UI
    def test_page_change(self, locator, url, obj_locator):
        self.page_change(locator, url, obj_locator)

