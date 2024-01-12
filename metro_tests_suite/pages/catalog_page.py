from selene import browser, have
from tests import conftest


class Catalog:
    browser = conftest.setup_browser

    def open_main_page(self):
        browser.open('/')
        return self

    def open_catalog(self):
        browser.element('[data-qa=header-catalog-button]').click()
        return self

    def select_the_catalog_position(self):
        browser.element('li:nth-child(6) span:nth-child(2)').click()
        return self

    def assert_catalog_section(self):
        browser.element(
            '.slider-main-block__heading--h1 .slider-main-block__heading-title'
        ).should(have.text('Мясо, птица, колбасы'))
        return self
