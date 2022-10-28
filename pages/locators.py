from selenium.webdriver.common.by import By


class Urls:
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"
    LOGIN_PAGE_URI = "/accounts/login/"
    LINKS_PROMO_OFFER = [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ]


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LOCATOR = (By.CSS_SELECTOR, ".basket-mini > span > .btn")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, ".product_main > h1")
    ALERT_THAT_PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages > .alert")
    ALERT_WITH_BASKET_PRICE = (By.CSS_SELECTOR, "#messages > .alert", 2)
    BASKET_PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, ".alertinner > strong")
    BASKET_PRODUCT_PRICE_LOCATOR = (By.CSS_SELECTOR, ".alertinner > p > strong")


class BasketPageLocators():
    PRODUCT_IN_BASKET_FORM = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_EMPTY_LOCATOR = (By.CSS_SELECTOR, "#content_inner > p")
