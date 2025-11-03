import pytest
from pages.cart_page import CartPage
from utils.logger import get_logger

LOG = get_logger(__name__)


@pytest.mark.order(4)
def test_remove_item(driver, base_url, pincode):
    driver.get(base_url)

    # Import placed inside the function to avoid circular imports
    from pages.home_page import HomePage

    home = HomePage(driver)
    home.set_pincode(pincode)

    cart = CartPage(driver)

    # Get cart count before removing item
    initial_count = cart.get_cart_count()
    LOG.info(f"Initial cart count: {initial_count}")

    # Remove first item
    cart.remove_first_item()
    LOG.info("Removed first item from cart")

    # Validate cart updated (initial_count should reduce by 1 ideally)
    final_count = cart.get_cart_count()
    LOG.info(f"Final cart count: {final_count}")

    assert final_count <= initial_count - 1 or final_count == 0, \
        "Cart item was not removed successfully"
