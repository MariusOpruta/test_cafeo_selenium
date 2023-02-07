

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By



class NewsletterPage:
    BUTTON_NEWSLETTER = (By.CSS_SELECTOR,'[class="button btn btn-add btn-newsletter"]')
    EMAIL_INPUT = (By.ID,"input-11")

    #FORM = (By.ID,"movalio-email-widget-1675687826213-327-12")
    FORM = (By.CLASS_NAME,"desktop visible relative email-signup-container")
    #FORM = (By.CSS_SELECTOR,'[class="desktop visible relative email-signup-container"]')

    SELECT_TERMS = (By.CLASS_NAME,"col col-1 align-self-start")
    LINK_TERMS = (By.CSS_SELECTOR,'[href="https://cafeo.ro/p/termeni"]')
    PAGE_TERMS = (By.CSS_SELECTOR,'[class="breadcrumb clearfix"]')  # Termeni și condiții de utilizare
    LINK_POLITICS = (By.CSS_SELECTOR,'[href="https://cafeo.ro/p/privacy"]')
    PAGE_POLITICS = (By.CSS_SELECTOR, '[class="breadcrumb clearfix"]')  #Politica de confidentialitate
    BUTTON_OK = (By.CSS_SELECTOR,"#container > div > div > div.v-card__actions.pt-0 > div > div > button")

    def __init__(self, browser):
        self.browser = browser

    def button_newsletter(self):
        self.browser.find_element(*self.BUTTON_NEWSLETTER).click()
    def switch(self):
        #self.browser.switch_to.frame('movalio-email-widget-1675687826213-327-12')

        # iframe = self.browser.find_element(By.ID,"movalio-email-widget-1675752669411-296-12")
        # self.browser.switch_to.frame(iframe)

        # self.browser.switch_to.frame('movalio-email-widget-1675687826213-327-12')

        iframe = self.browser.find_element(By.CSS_SELECTOR,"#overlay > iframe")
        self.browser.switch_to.frame(iframe)

    def email_input(self,email):
        self.browser.find_element(self.EMAIL_INPUT).send_keys(email)

    def click_select_terms(self):
        self.browser.find_element(*self.SELECT_TERMS).click()

    def click_link_terms(self):
        self.browser.find_element(*self.LINK_TERMS).click()

    def get_page_terms(self):
        self.browser.switch_to(*self.LINK_TERMS)
        return self.browser.find_element(*self.PAGE_TERMS).text

    def click_link_politics(self):
        self.browser.find_element(*self.LINK_POLITICS).click()

    def get_page_politics(self):
        self.browser.switch_to(*self.LINK_POLITICS)
        return self.browser.find_element(*self.PAGE_POLITICS).text


    def click_buton_ok(self):
        self.browser.find_element(*self.BUTTON_OK).click()
