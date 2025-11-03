from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    # Not heavily used in simple tests; placeholder for future
    ADD_BUTTON = (By.XPATH, "//button[contains(., 'Add')]")


    def add_to_cart(self):
        self.click(*self.ADD_BUTTON)