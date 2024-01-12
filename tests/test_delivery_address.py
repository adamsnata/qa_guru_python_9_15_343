import allure
from metro_tests_suite.pages.delivery_address_page import DeliveryAddress


@allure.title('Enter the new delivery address')
def test_enter_delivery_address():
    delivery_address = DeliveryAddress()

    with allure.step('Open main page'):
        delivery_address.open_main_page()

    with allure.step('Enter new delivery address'):
        delivery_address.enter_new_delivery_address(
            'Санкт-Петербург, Лиговский проспект, 50'
        )

    with allure.step('Assert new delivery address'):
        delivery_address.assert_new_address('Санкт-Петербург, Лиговский проспект, 50')
