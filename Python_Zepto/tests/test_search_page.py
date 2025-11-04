import pytest
from pages.searchpage import SearchPage
from utilities.action_helper import ActionHelper
from selenium import webdriver
import time
class TestZeptoSearch:
    def setup_method(self):
        # Initialize WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.zeptonow.com/")
        self.helper = ActionHelper(self.driver)
        time.sleep(3)
    def teardown_method(self):
        self.driver.quit()
        print("Browser closed successfully.")
    def test_search_functionality(self):
        print("Running Zepto Search Test for: milk")
        search_page = SearchPage(self.driver, self.helper)
        try:
            self.helper.take_screenshot("Before_Search")
            search_page.search_product("milk")
            self.helper.take_screenshot("After_Search")
            print("✅ Search executed successfully.")
        except Exception as e:
            self.helper.take_screenshot("Search_Failed")
            pytest.fail(f" Test failed due to: {str(e)}")
