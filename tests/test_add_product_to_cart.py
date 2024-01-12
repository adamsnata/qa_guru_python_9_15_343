import allure
from metro_tests_suite.pages.product_page import Product


@allure.title('Add product to cart (unregistered user)')
def test_add_product():
    product = Product()

    with allure.step('Open main page'):
        product.open_main_page()

    with allure.step('Enter the product name'):
        product.search_product('METRO Chef Мороженое Пломбир ванильный, 2.5кг')

    with allure.step('Add to cart'):
        product.add_to_cart()

    with allure.step('Enter the delivery address'):
        product.enter_the_delivery_address('Санкт-Петербург, Лиговский проспект, 50')

    with allure.step('Click to the cart icon'):
        product.click_to_the_cart()

    with allure.step('Checkout'):
        product.click_to_the_checkout_button()

    with allure.step('Assert'):
        product.assert_checkout()


@allure.title('Add product to cart with pickup')
def test_add_product_to_cart_with_pickup():
    product = Product()

    with allure.step('Open main page'):
        product.open_main_page()

    with allure.step('Enter the product name'):
        product.search_product('METRO Chef Лапша гречневая, 600г')

    with allure.step('Add to cart'):
        product.add_to_cart()

    with allure.step('Change delivery to pickup'):
        product.click_to_the_pickup_button()
