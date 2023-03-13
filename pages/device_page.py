from selenium.webdriver.common.by import By
class DevicePage:
    Device_CLICK = (By.CSS_SELECTOR,'[href="https://cafeo.ro/aparate/"]')
    BRAND_CHECK = (By.ID,"uniform-layered_manufacturer_70")
    ADD_CLICK = (By.CSS_SELECTOR,"#center_column > ul > li > div > div.action-button.clearfix > a")
    TITLE_TEXT = (By.CLASS_NAME,"breadcrumb-category")
    CONFIRM_TEXT = (By.CSS_SELECTOR,'h2')
    BASKET_DETAIL_CLICK = (By.CSS_SELECTOR,"#layer_cart > div.clearfix > div.layer_cart_cart.col-xs-12 > div.button-container > a")
    TOTAL_PRICE_TEXT = (By.CSS_SELECTOR,"#cart_summary > tfoot")

    def __init__(self, browser):
        self.browser = browser

    def device_click(self):
        self.browser.find_element(*self.Device_CLICK).click()

    def brand_check(self):
        self.browser.find_element(*self.BRAND_CHECK).click()

    def title_check(self):
        return self.browser.find_element(*self.TITLE_TEXT).text

    def add_click(self):
        self.browser.find_element(*self.ADD_CLICK).click()

    def confirm(self):
        return self.browser.find_element(*self.CONFIRM_TEXT).text

    def detail_basket(self):
        self.browser.find_element(*self.BASKET_DETAIL_CLICK).click()

    def total_check(self):
        return self.browser.find_element(*self.TOTAL_PRICE_TEXT).text



