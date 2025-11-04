import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class SearchPage:
    def __init__(self, driver, helper):
        self.driver = driver
        self.helper = helper

        # Correct XPaths (verified)
        self.search_icon = (By.XPATH, "/html/body/div[1]/div/div/div/div/header/div/div[2]/a")
        self.search_input = (By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/input")

    def search_product(self, product_name):
        print("Opening Zepto search bar...")
        try:
            self.helper.click(self.search_icon, "Search Icon")
            time.sleep(2)

            print(f"Typing '{product_name}' in search bar...")
            self.helper.type(self.search_input, product_name, "Search Box")
            self.helper.press_enter(self.search_input)

            print("Waiting for search results...")
            time.sleep(4)
            self.helper.take_screenshot("SearchResults")

        except TimeoutException:
            print("Could not locate the search box or icon.")
