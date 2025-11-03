import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from utils.logger import get_logger


LOG = get_logger(__name__)


@pytest.mark.order(1)
def test_search_and_add(driver, base_url, pincode):
        home = HomePage(driver)
        search = SearchResultsPage(driver)


        home.open(base_url)
        LOG.info('Opened base URL')
        home.set_pincode(pincode)
        LOG.info(f'Set pincode {pincode}')


        home.search('Milk')
        assert search.has_results(), 'No search results found for Milk'
        LOG.info('Search returned results')


        search.add_first_product()
        LOG.info('Added first product')