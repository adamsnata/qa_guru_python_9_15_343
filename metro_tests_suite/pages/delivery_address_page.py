from selene import browser, have
from tests import conftest
import time


class DeliveryAddress:
    browser = conftest.setup_browser

    def open_main_page(self):
        browser.open('/')
        return self

    def enter_new_delivery_address(self, value):
        browser.element('.header-address .header-address__receive-button').click()
        browser.element('#search-input').type(value).press_enter()
        time.sleep(2)
        browser.element('[data-qa=button-save-delivery-address]').click()
        return self

    def assert_new_address(self, value):
        browser.element('.header-address .header-address__receive-address').should(
            have.text(value)
        )
        return self
