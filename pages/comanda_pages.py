from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.devtools.v85.indexed_db import Key


class ComandaNoua:
    SELECT_BRAND = (By.CSS_SELECTOR,'[src="/img/brands/morra.png"]')
    SELECT_PRODUCT = (By.CSS_SELECTOR,'[src="https://cafeo.ro/2337-home_default/morra-espresso-cafea-boabe-1kg.jpg"]')
    CANTITATE = (By.ID,"quantity_wanted_p")
    CANTITATE_SELECT = (By.NAME,"qty")
    NUMAR_CANTITATE = (By.CSS_SELECTOR,"#quantity_wanted > option:nth-child(3)")
    ADAUGA_COS = (By.CSS_SELECTOR,'[class="buttons_bottom_block no-print"]')
    MESAJ_ADAUGAT = (By.CSS_SELECTOR,'[class="layer_cart_product col-xs-12"]')   #"Produsul a fost adăugat în coș"
    BUTON_DETALI_COS = (By.CSS_SELECTOR,'[class="ajax-proceed-comanda btn btn-default button button-medium button-action ga-track"]')

    def __init__(self, browser):
        self.browser = browser

    def click_select_brand(self):
        self.browser.find_element(*self.SELECT_BRAND).click()

    def click_select_product(self):
        self.browser.find_element(*self.SELECT_PRODUCT).click()

    def cantitate(self):
        self.browser.find_element(*self.CANTITATE).click()

    def click_cantitate(self):
        self.browser.find_element(*self.CANTITATE_SELECT).click()

    def select_numar_bucati(self):
        self.browser.find_element(*self.NUMAR_CANTITATE).send_keys(Keys.ENTER)

    def click_adauga_cos(self):
        self.browser.find_element(*self.ADAUGA_COS).click()

    def get_mesaj_adaugat(self):
        return self.browser.find_element(*self.MESAJ_ADAUGAT).text

    def click_buton_detalii_cos(self):
        self.browser.find_element(*self.BUTON_DETALI_COS).click()






