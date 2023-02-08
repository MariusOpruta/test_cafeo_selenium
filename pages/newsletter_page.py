from selenium.webdriver.common.by import By


class NewsletterPage:
    BUTTON_NEWSLETTER = (By.CSS_SELECTOR,'[class="button btn btn-add btn-newsletter"]')
    IFRAME = (By.CSS_SELECTOR, "iframe[id^='movalio-email-widget']")
    EMAIL_INPUT = (By.ID,"input-11")
    SELECT_TERMS = (By.CSS_SELECTOR, "div.v-input--selection-controls__input")
    LINK_TERMS = (By.CSS_SELECTOR,'[href="https://cafeo.ro/p/termeni"]')
    PAGE_TERMS = (By.CSS_SELECTOR,'[class="cms cms-3 cms-termeni lang_ro  "]')  # Termeni și condiții de utilizare
    LINK_POLITICS = (By.CSS_SELECTOR,'[href="https://cafeo.ro/p/privacy"]')
    PAGE_POLITICS = (By.CSS_SELECTOR, '[class="breadcrumb clearfix"]')  #Politica de confidentialitate
    BUTTON_OK = (By.CSS_SELECTOR,"#container > div > div > div.v-card__actions.pt-0 > div > div > button")
    #BUTTON_OK = (By.CLASS_NAME, "v-btn v-btn--depressed theme--light v-size--x-large primary px-6")
    def __init__(self, browser):
        self.browser = browser

    def button_newsletter(self):
        self.browser.find_element(*self.BUTTON_NEWSLETTER).click()
    def switch(self):
        iframe = self.browser.find_element(By.CSS_SELECTOR, "iframe[id^='movalio-email-widget']")
        self.browser.switch_to.frame(iframe)

    def email_input(self,email):
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_select_terms(self):
        self.browser.find_element(*self.SELECT_TERMS).click()

    def click_link_terms(self):
        self.browser.find_element(*self.LINK_TERMS).click()

    def schimb_page_terms(self):
        for handle in self.browser.window_handles:
            self.browser.switch_to.window(handle)
        # window = self.browser.find_element(By.CSS_SELECTOR,'[class="cms cms-3 cms-termeni lang_ro  "]')
        # self.browser.switch_to.frame(window)
    def get_page_terms(self):
        return self.browser.find_element(*self.PAGE_TERMS).text


    def click_link_politics(self):
        self.browser.find_element(*self.LINK_POLITICS).click()

    def get_page_politics(self):
        return self.browser.find_element(*self.PAGE_POLITICS).text

    def return_page(self):
        p= self.browser.window_handles[0]
        c = self.browser.window_handles[1]
        self.browser.switch_to.window(c)
        self.browser.close()
        self.browser.switch_to.window(p)
        self.browser.switch_to.frame(self.browser.find_element(*self.IFRAME))
    def click_buton_ok(self):
        self.browser.find_element(*self.BUTTON_OK).click()
