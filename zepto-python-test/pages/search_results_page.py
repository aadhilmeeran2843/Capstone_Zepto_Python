from selenium.webdriver.common.by import By
from .base_page import BasePage


class SearchResultsPage(BasePage):
    ADD_BUTTONS = (By.XPATH, "//button[contains(., 'Add')]")
    PRODUCT_TITLES = (By.XPATH, "//a[contains(@href, '/p/') or contains(@class,'product-card')]//h3 | //h3")


    def add_first_product(self):
        buttons = self.find_all(*self.ADD_BUTTONS)
        buttons[0].click()


    def has_results(self):
        elems = self.find_all(*self.PRODUCT_TITLES)
        return len(elems) > 0