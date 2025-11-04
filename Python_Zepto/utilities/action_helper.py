import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionHelper:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, description=""):
        element = self.wait_for_element(locator)
        element.click()
        print(f"Clicked on: {description}")

    def type(self, locator, text, description=""):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
        print(f"Entered '{text}' in {description}")

    def press_enter(self, locator):
        element = self.wait_for_element(locator)
        element.send_keys(Keys.ENTER)
        print("Pressed Enter")

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        path = f"reports/{name}_{timestamp}.png"
        self.driver.save_screenshot(path)
        print(f"Screenshot saved at: {path}")
