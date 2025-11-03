import pytest
from pages.cart_page import CartPage
from utils.logger import get_logger


LOG = get_logger(__name__)


@pytest.mark.order(3)
def test_change_quantity(driver, base_url, pincode):
    driver.get(base_url)
    from pages.home_page import HomePage
    home = HomePage(driver)
    home.set_pincode(pincode)


    cart = CartPage(driver)
    # attempt to increase quantity
    cart.increase_first_item()
    LOG.info('Increased quantity for first cart item')
    # you could assert quantity changed if locator stable