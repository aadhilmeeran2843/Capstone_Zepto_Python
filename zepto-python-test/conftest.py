import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from utils.logger import get_logger

LOG = get_logger(__name__)


def pytest_addoption(parser):
    parser.addoption('--base-url', action='store', default='https://www.zeptonow.com/',
                     help='Base URL for tests')
    parser.addoption('--pincode', action='store', default='560066',
                     help='Pincode to use')


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption('--base-url')


@pytest.fixture(scope='session')
def pincode(request):
    return request.config.getoption('--pincode')


@pytest.fixture(scope='function')
def driver(request):
    """Create a Chrome WebDriver instance using webdriver-manager"""
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    # chrome_options.add_argument('--headless')  # Enable if needed

    service = ChromeService(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=chrome_options)
    LOG.info('Launching Chrome Browser')

    yield drv

    LOG.info('Closing Chrome Browser')
    drv.quit()


# ✅ Screenshot on test failure
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # Execute internal pytest hooks
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        try:
            drv = item.funcargs.get('driver')
            if drv:
                screenshots_dir = os.path.join('reports', 'screenshots')
                os.makedirs(screenshots_dir, exist_ok=True)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = os.path.join(screenshots_dir, f"{item.name}_{timestamp}.png")
                drv.save_screenshot(filename)
                LOG.error(f"Screenshot captured: {filename}")
        except Exception as e:
            LOG.exception(f"Failed to capture screenshot: {e}")
