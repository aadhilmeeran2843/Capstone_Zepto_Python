# import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys

        def test_zepto_search_and_add():
            driver = webdriver.Chrome(executable_path="./drivers/chromedriver.exe")
            driver.maximize_window()

            # 1️⃣ Open Zepto
            driver.get("https://www.zeptonow.com/")
            time.sleep(3)

            # 2️⃣ Select location (sample pincode)
            location_box = driver.find_element(By.XPATH, "//input[@placeholder='Enter your address or area']")
            location_box.send_keys("560066")
            time.sleep(2)
            location_box.send_keys(Keys.ENTER)
            time.sleep(5)

            # 3️⃣ Search for "Milk"
            search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search for items']")
            search_box.send_keys("Milk")
            search_box.send_keys(Keys.ENTER)
            time.sleep(4)

            # 4️⃣ Add the first product shown
            add_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Add')]")
            assert len(add_buttons) > 0, "No products found!"
            add_buttons[0].click()
            time.sleep(3)

            # ✅ 5️⃣ Verify Cart icon shows count
            cart_badge = driver.find_element(By.XPATH, "//span[contains(@class,'CartItemCount')]")
            assert cart_badge.text != "0", "Item not added!"

    driver.quit()
