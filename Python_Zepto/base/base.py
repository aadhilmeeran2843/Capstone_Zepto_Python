from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.action_helper import ActionHelper


class BaseTest:
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.helper = ActionHelper(self.driver)

        # Open Zepto website
        self.driver.get("https://www.zeptonow.com/")
        print("Zepto website launched successfully.")

    def run_zepto_test(self):
        print("Running Zepto automation test...")

    def teardown_method(self):
        self.driver.quit()
        print("Browser closed successfully.")
