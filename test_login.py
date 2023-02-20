from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from setup_login import driver, braip_prod, braip_maps, email, senha
import unittest


class LoginTest(unittest.TestCase):


    def test_login_bem_sucedido(self):
        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            title = driver.title

            if title == 'Braip members - Home':
                driver.save_screenshot('screen_00.png')
            else:
                driver.get(braip_prod)
                time.sleep(1)
                field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
                field_login.send_keys(email)
                field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
                field_password.send_keys(senha)
                field_password.send_keys(Keys.RETURN)
                driver.save_screenshot('screen_00.png')
                time.sleep(3)
                
            try:
                title = driver.title
                assert 'Braip members - Home' in title
                print(title)
                driver.save_screenshot('screen_01.png')
                break
            except:
                print(title)
                attempts += 1
                if attempts == max_attempts:
                    print('Failed to log in after {} attempts'.format(max_attempts))
                    raise