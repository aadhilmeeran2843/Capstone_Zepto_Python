from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    LOCATION_INPUT = (By.XPATH, "//input[@placeholder='Enter your address or area']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search for items']")


    def open(self, url):
        self.driver.get(url)


    def set_pincode(self, pincode):
        self.type(*self.LOCATION_INPUT, text=pincode)
        # Press Enter
        self.find(*self.LOCATION_INPUT).send_keys('\n')


    def search(self, text):
        self.type(*self.SEARCH_INPUT, text=text)
        self.find(*self.SEARCH_INPUT).send_keys('\n')