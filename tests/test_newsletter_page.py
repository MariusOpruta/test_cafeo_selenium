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
    newsletter.email_input('aaaa@yahoo.com')
    newsletter.click_select_terms()
    newsletter.click_link_terms()
    newsletter.schimb_page_terms()
    assert "Termeni și condiții de utilizare" in newsletter.get_page_terms()
    newsletter.click_link_politics()
    newsletter.schimb_page_terms()
    assert "Politica de confidentialitate" in newsletter.get_page_politics()
    newsletter.return_page()
    newsletter.click_buton_ok()
