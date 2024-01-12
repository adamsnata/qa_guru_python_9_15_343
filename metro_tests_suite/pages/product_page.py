from selene import browser, have, be
from tests import conftest
import time


class Product:
    browser = conftest.setup_browser

    def open_main_page(self):
        browser.open('/')
        return self

    def search_product(self, value):
        browser.element('[data-qa=header-search-input]').should(be.blank).type(
            value
        ).press_enter()
        return self

    def add_to_cart(self):
        browser.element('.product-card__content .simple-button__text').click()
        return self

    def enter_the_delivery_address(self, value):
        browser.element('#search-input').type(value).press_enter()
        time.sleep(2)
        browser.element('[data-qa=button-save-delivery-address]').click()
        return self

    def click_to_the_cart(self):
        browser.element('[data-qa=header-cart-button]').press_enter()
        return self

    def click_to_the_checkout_button(self):
        browser.element('[data-qa=header-cart-popup-link-checkout]').click()
        return self

    def assert_checkout(self):
        browser.element('.auth-modal__column .auth-subtitle').should(
            have.text('Введите номер телефона, чтобы войти или зарегистрироваться')
        )
        return self

    def click_to_the_pickup_button(self):
        browser.element(
            '.obtainments-list__item:nth-child(2) .obtainments-list__description'
        ).click()
        browser.element('[data-qa=button-save-pickup-address]').click()
        return self
