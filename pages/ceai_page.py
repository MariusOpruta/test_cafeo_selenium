from selenium.webdriver.common.by import By


class CeaiPage:
    CEAI_LIST = (By.CSS_SELECTOR, '[href="https://cafeo.ro/ceai/"]')
    CEAI_INFUZABIL = (By.CSS_SELECTOR, '[href="https://cafeo.ro/ceai/ceai-infuzabil/"]')
    SELECT_CEAI = (By.CSS_SELECTOR, '#center_column > ul > li:nth-child(2)')
    SELECT_CANTITATE = (By.CSS_SELECTOR, "#quantity_wanted")
    BUTON_ADAUGA = (By.CSS_SELECTOR, "#add_to_cart > button")
    MESAJ_OK = (By.CSS_SELECTOR, 'h2')

    def __init__(self, browser):
        self.browser = browser

    def ceai_list(self):
        self.browser.find_element(*self.CEAI_LIST).click()

    def select_ceai_fel(self):
        self.browser.find_element(*self.SELECT_CEAI).click()

    def aleg_cantitate(self, element):
        self.browser.find_element(*self.SELECT_CANTITATE).send_keys(element)

    def click_buton_adauga(self):
        self.browser.find_element(*self.BUTON_ADAUGA).click()

    def get_mesaj_ok(self):
        return self.browser.find_element(*self.MESAJ_OK).text
