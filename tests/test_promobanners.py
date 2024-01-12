import allure
from metro_tests_suite.pages.promo_page import Promo


@allure.title('Happy new year promobanner')
def test_promobanners():

    promo_banners = Promo()

    with allure.step('Open main page'):
        promo_banners.open_main_page()

    with allure.step('Swipe promobanners'):
        promo_banners.swipe_promobanners()

    with allure.step('Select the happy new year promobanner'):
        promo_banners.select_the_promobanner()

    with allure.step('Assert selected promobanner'):
        promo_banners.assert_selected_promobanner()
