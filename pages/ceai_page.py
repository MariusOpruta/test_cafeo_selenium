from selenium.webdriver.common.by import By

class CeaiPage:
    CEAI_LIST = (By.CSS_SELECTOR,"#block_top_menu > ul > li.sfHoverForce")
    CEAI_INFUZABIL = (By.CSS_SELECTOR,'[href="https://cafeo.ro/ceai/ceai-infuzabil/"]')
    SELECT_CEAI = (By.CSS_SELECTOR,'[src="https://cafeo.ro/2413-home_default/eilles-tea-assam-special-teebeutel-25-plicuri.jpg"]')
    SELECT_CANTITATE = (By.CSS_SELECTOR,"#quantity_wanted")
    BUTON_ADAUGA = (By.CSS_SELECTOR,"#add_to_cart > button")

    def __init__(self, browser):
        self.browser = browser

    def ceai_list(self):
        self.browser.find_element(*self.CEAI_LIST).click()

    def select_ceai_fel(self):
        self.browser.find_element(*self.SELECT_CEAI).click()

    def aleg_cantitate(self,element):
        self.browser.find_element(*self.SELECT_CANTITATE).send_keys(element)

    def click_buton_adauga(self):
        self.browser.find_element(*self.BUTON_ADAUGA).click()
