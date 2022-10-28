from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        basket_button.click()

    def should_be_product_name_and_price(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_LOCATOR
        ).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_LOCATOR
        ).text
        print(product_name)
        print(product_price)

    def should_be_alert_that_product_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_THAT_PRODUCT_ADD_TO_BASKET
        )

    def should_be_alert_with_basket_price(self):
        assert self.is_element_present2(*ProductPageLocators.ALERT_WITH_BASKET_PRICE)

    def is_product_price_the_same(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_LOCATOR
        ).text
        product_price_in_basket = self.browser.find_element(
            *ProductPageLocators.BASKET_PRODUCT_PRICE_LOCATOR
        ).text
        assert product_price == product_price_in_basket

    def is_product_name_the_same(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_LOCATOR
        ).text
        product_name_in_basket = self.browser.find_element(
            *ProductPageLocators.BASKET_PRODUCT_NAME_LOCATOR
        ).text
        assert product_name == product_name_in_basket

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_THAT_PRODUCT_ADD_TO_BASKET), "Success message is presented, but should not be"

    def success_message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_THAT_PRODUCT_ADD_TO_BASKET), "Success message should dissapear, but it doesnt"
