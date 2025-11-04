from base.base import BaseTest

class TestZepto(BaseTest):

    def test_open_zepto_homepage(self):
        self.setup_method()  # Setup browser
        self.driver.get("https://www.zeptonow.com/")
        assert "Zepto" in self.driver.title  # Basic check
        print("✅ Zepto homepage opened successfully")
        self.teardown_method()  # Close browser
