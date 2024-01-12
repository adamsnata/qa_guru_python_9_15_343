from selene import browser, have
from tests import conftest


class Promo:
    browser = conftest.setup_browser

    def open_main_page(self):
        browser.open('/')
        return self

    def swipe_promobanners(self):
        browser.element('.swiper-pagination-bullet:nth-child(2)').click()
        return self

    def select_the_promobanner(self):
        browser.element('.swiper-slide:nth-child(5) .promobanners-slider-item').click()
        return self

    def assert_selected_promobanner(self):
        browser.element('.subcategory-or-type__heading-title').should(
            have.text('Бренди и коньяк до -40%')
        )
        return self
