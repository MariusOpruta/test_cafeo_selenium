from time import sleep

from pages.home_page import HomePage
from pages.device_page import DevicePage


def test_device_page(browser):
    home_page = HomePage(browser)
    device = DevicePage(browser)
    home_page.load_page()
    device.device_click()
    device.brand_check()
    assert "Aparate cafea" in device.title_check()
    device.add_click()
    sleep(4)
    assert "Produsul a fost adăugat în coș" in device.confirm()
    device.detail_basket()
    assert "TOTAL" in device.total_check()

