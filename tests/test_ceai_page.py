from time import sleep

from pages.home_page import HomePage
from pages.ceai_page import CeaiPage
from pages.comanda_pages import ComandaNoua

def test_ceai(browser):
    home_page = HomePage(browser)
    comanda = ComandaNoua(browser)
    ceai = CeaiPage(browser)
    home_page.load_page()
    sleep(4)
    ceai.ceai_list()
    ceai.select_ceai_fel()
    ceai.aleg_cantitate(3)
    ceai.click_buton_adauga()
    sleep(4)
    assert "Produsul a fost adăugat în coș" in ceai.get_mesaj_ok()
