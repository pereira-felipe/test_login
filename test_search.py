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
            login_test = LoginTest()
            login_test
            field_search = driver.find_element(By.XPATH, braip_maps ["buttons"]["send_search"]["xpath"])
            field_search.click()
            driver.save_screenshot('screen_09.png')
            field_search_key = driver.find_element(By.XPATH, braip_maps ["buttons"]["send_search_key"]["xpath"])
            field_search_key.send_keys('aula')
            field_search_key.send_keys(Keys.RETURN)
            time.sleep(1)

            try:
                title = driver.title
                assert'Braip Members - Resultados da Busca' in title
                print(title)
                driver.save_screenshot('screen_01.png')
                break
            except:
                attempts += 1
                print(title)


        if attempts == max_attempts:
            raise Exception("Failed to log in after {} attempts".format(max_attempts))