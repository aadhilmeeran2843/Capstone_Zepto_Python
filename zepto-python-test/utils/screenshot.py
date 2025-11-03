import os
from datetime import datetime




def save_screenshot(driver, name_prefix='screenshot'):
    screenshots_dir = os.path.join(os.getcwd(), 'reports', 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)
    filename = f"{name_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    path = os.path.join(screenshots_dir, filename)
    driver.save_screenshot(path)
    return path