from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from setup_login import driver, braip_maps
import unittest
from test_login import LoginTest


class SearchTest(unittest.TestCase):


    def test_login_bem_sucedido_search(self):
        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            LoginTest
            field_search = driver.find_element(By.XPATH, braip_maps ["buttons"]["send_search"]["xpath"])
            field_search.click()
            driver.save_screenshot('screen_10.png')
            field_search_key = driver.find_element(By.XPATH, braip_maps ["buttons"]["send_search_key"]["xpath"])
            field_search_key.send_keys('aula')
            field_search_key.send_keys(Keys.RETURN)
            time.sleep(1)

            try:
                title = driver.title
                assert'Braip Members - Resultados da Busca' in title
                print(title)
                driver.save_screenshot('screen_11.png')
                home = driver.find_element(By.XPATH,braip_maps["buttons"]["home"]["xpath"])
                home.click()
                time.sleep(1)
                print('cheguei')
                break
            except:
                attempts += 1
                print(title)
                if attempts == max_attempts:
                    raise