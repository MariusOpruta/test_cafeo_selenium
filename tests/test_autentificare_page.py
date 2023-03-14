from time import sleep

from pages.autentificare_page import AutentificarePage
from pages.home_page import HomePage
from pages.cont_nou_page import ContNouPage


def test_login_with_invalid_credentials_no_username_no_password(browser):
    home_page = HomePage(browser)
    customer_page = AutentificarePage(browser)
    home_page.load_page()
    home_page.click_contul_meu_button()
    sleep(4)
    customer_page.click_intra_in_cont()
    sleep(5)
    assert "Adresa de e-mail este obligatorie" in customer_page.get_error_message_text()


def test_login_with_invalid_credentials(browser):
    home_page = HomePage(browser)
    customer_page = AutentificarePage(browser)
    home_page.load_page()
    home_page.click_contul_meu_button()
    customer_page.type_email("ion@ion.com")
    customer_page.type_password("start123")
    customer_page.click_intra_in_cont()
    sleep(5)
    assert "Adresa de email sau parola sunt greșite. Încearcă din nou." in customer_page.get_error_message_text()


def test_login_with_new_data(browser):
    home_page = HomePage(browser)
    new_data_page = ContNouPage(browser)
    home_page.load_page()
    home_page.click_contul_meu_button()
    new_data_page.email_creaza_cont("x55799BW6.hb0123@yahoo.com")
    new_data_page.creaza_cont_buton()
    sleep(4)
    new_data_page.selecteaza_buton_radio()
    new_data_page.input_prenume("a")
    new_data_page.input_nume("b")
    new_data_page.input_passwd_cont_nou("1923456")
    new_data_page.valid_terms_conditions()
    new_data_page.valid_years()
    new_data_page.click_create_button()
    sleep(5)
    assert "Bine ai venit în contul tău. " in new_data_page.mesage_valid_text()
    assert "Contul dumneavoastră a fost creat." in new_data_page.message_ok()


def test_login_with_valid_data(browser):
    home_page = HomePage(browser)
    new_data_page = ContNouPage(browser)
    customer_page = AutentificarePage(browser)
    home_page.load_page()
    home_page.click_contul_meu_button()
    customer_page.type_email("x55799bw3.hb123@yahoo.com")
    customer_page.type_password("1923456")
    customer_page.click_intra_in_cont()
    sleep(5)
    assert "Aici poți modifica informațiile personale " in new_data_page.mesage_valid_text()
    customer_page.valid_info()
    sleep(4)
    assert "Informații personale" in customer_page.get_email()
