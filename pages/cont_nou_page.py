import email

from selenium.webdriver.common.by import By

class ContNouPage:
    NEW_EMAIL_IMPUT = (By.ID,'email_create')
    CONT_NOU_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-default button button-medium button-2action exclusive"]')
    SELECT_RADIO_BUTTON = (By.CSS_SELECTOR,"#uniform-id_gender1")
    PRENUME_INPUT = (By.ID,"customer_firstname")
    NUME_INPUT = (By.ID,"customer_lastname")
    PAROLA_CREARE_CONT = (By.CSS_SELECTOR,"#passwd")
    CHECK_TERMS = (By.ID,"agree_terms")
    CHECK_YEARS = (By.ID,"agree_age")
    CREATE_CONT_BUTTON = (By.ID,"submitAccount")
    MESAGE_VALID = (By.CSS_SELECTOR, "#center_column > p.alert.alert-success")
    def __init__(self, browser):
        self.browser = browser

    def email_creaza_cont(self,email):
        self.browser.find_element(*self.NEW_EMAIL_IMPUT).send_keys(email)

    def creaza_cont_buton(self):
        self.browser.find_element(*self.CONT_NOU_BUTTON).click()

    def selecteaza_buton_radio(self):
        self.browser.find_element(*self.SELECT_RADIO_BUTTON).click()

    def input_prenume(self, prenume):
        self.browser.find_element(*self.PRENUME_INPUT).send_keys(prenume)

    def input_nume(self, nume):
        self.browser.find_element(*self.NUME_INPUT).send_keys(nume)

    def input_passwd_cont_nou(self, passwd):
        self.browser.find_element(*self.PAROLA_CREARE_CONT).send_keys(passwd)

    def valid_terms_conditions(self):
        self.browser.find_element(*self.CHECK_TERMS).click()

    def valid_years(self):
        self.browser.find_element(*self.CHECK_YEARS).click()

    def click_create_button(self):
        self.browser.find_element(*self.CREATE_CONT_BUTTON).click()

    def mesage_valid_text(self):
        self.browser.find_element(*self.MESAGE_VALID).text





