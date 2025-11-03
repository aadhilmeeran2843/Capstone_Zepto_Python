import pytest
from pages.cart_page import CartPage
from utils.logger import get_logger


LOG = get_logger(__name__)


@pytest.mark.order(2)
def test_verify_cart_count(driver, base_url, pincode):
    driver.get(base_url)
    # set pincode again if needed
    from pages.home_page import HomePage
    home = HomePage(driver)
    home.set_pincode(pincode)


    cart = CartPage(driver)
    count = cart.get_cart_count()
    assert int(count) >= 1, 'Cart count is less than 1 after adding item'
    LOG.info(f'Cart count is {count}')