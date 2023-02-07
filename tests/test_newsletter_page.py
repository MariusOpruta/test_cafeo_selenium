from time import sleep

from pages.home_page import HomePage
from pages.newsletter_page import NewsletterPage

def test_newsletter_page(browser):
    home_page = HomePage(browser)
    newsletter = NewsletterPage(browser)
    home_page.load_page()
    sleep(5)
    newsletter.button_newsletter()
    sleep(5)
    newsletter.switch()
    newsletter.email_introduc("aaaa@yahoo.com")
    newsletter.click_select_terms()
    sleep(4)
    newsletter.click_link_terms()
    sleep(4)
    # assert "Termeni și condiții de utilizare" in newsletter.get_page_terms()
    # sleep(4)
    #sleep(4)
    newsletter.click_link_politics()
    sleep(4)
    # assert "Politica de confidentialitate" in newsletter.get_page_politics()
    # browser.close()
    newsletter.click_buton_ok()