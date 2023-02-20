from selenium.webdriver.common.by import By
import time
from setup_login import driver, braip_maps
import unittest
from test_login import LoginTest


class FavoritesTest(unittest.TestCase):


    def test_login_bem_sucedido_favorites(self):
        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            LoginTest
            time.sleep(2)
            field_favorites = driver.find_element(By.XPATH,braip_maps["buttons"]["send_favorites"]["xpath"])
            field_favorites.click()
            time.sleep(1)

            try:
                title = driver.title
                assert 'Braip Members - Favoritos' in title
                print(title)
                driver.save_screenshot('screen_07.png')
                home = driver.find_element(By.XPATH,braip_maps["buttons"]["home"]["xpath"])
                home.click()
                time.sleep(1)
                break
            except:
                attempts += 1
                print(title)
                if attempts == max_attempts:
                    raise