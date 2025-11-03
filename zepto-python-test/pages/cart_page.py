from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    CART_COUNT = (By.XPATH, "//span[contains(@class,'CartItemCount') or @data-testid='cart-count']")
    INCREASE_QTY = (By.XPATH, "//button[contains(., '+') or contains(@aria-label,'increase')]")
    DECREASE_QTY = (By.XPATH, "//button[contains(., '-') or contains(@aria-label,'decrease')]")
    REMOVE_BTN = (By.XPATH, "//button[contains(., 'Remove') or contains(., 'REMOVE')]")


    def get_cart_count(self):
        el = self.find(*self.CART_COUNT)
        text = el.text.strip()
        try:
            return int(text)
        except:
            return text


    def increase_first_item(self):
        self.click(*self.INCREASE_QTY)


    def remove_first_item(self):
        self.click(*self.REMOVE_BTN)