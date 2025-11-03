import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    def find(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))


    def find_all(self, by, value):
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))


    def click(self, by, value):
        el = self.find(by, value)
        el.click()
        return el


    def type(self, by, value, text):
            el = self.find(by, value)
            el.clear()
            el.send_keys(text)
            return el