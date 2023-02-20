from selenium.webdriver.common.by import By
import time
from setup_login import driver, braip_maps
import unittest
from test_login import LoginTest


class LikeTest(unittest.TestCase):


    def test_login_bem_sucedido_like(self):
        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            LoginTest            
            time.sleep(1)
            field_like = driver.find_element(By.XPATH,braip_maps["buttons"]["send_like"]["xpath"])
            field_like.click
            time.sleep(1)

            try:
                title = driver.title
                assert 'Braip members - Home' in title
                print(title)
                driver.save_screenshot('screen_08.png')
                break
            except:
                attempts += 1
                print(title)
                if attempts == max_attempts:
                    raise