from selenium.webdriver.common.by import By
import time
from setup_login import driver, braip_maps
import unittest
from test_login import LoginTest


class MyAccountTest(unittest.TestCase):


    def test_login_bem_sucedido_my_account(self):
        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            LoginTest
            time.sleep(2)
            field_perfil = driver.find_element(By.XPATH,braip_maps["buttons"]["perfil"]["xpath"])
            field_perfil.click()
            time.sleep(1)
            field_logout = driver.find_element(By.XPATH,braip_maps["buttons"]["account"]["xpath"])
            field_logout.click
            field_logout = driver.find_element(By.XPATH,braip_maps["buttons"]["close"]["xpath"])
            field_logout.click()

            try:
                time.sleep(1)
                title = driver.title
                print(title)
                assert 'Braip members - Home' in title
                driver.save_screenshot('screen_07.png')
                time.sleep(1)
                break
            except:
                attempts += 1
                print(title)
                if attempts == max_attempts:
                    raise