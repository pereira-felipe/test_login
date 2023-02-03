from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from setup_login import driver, braip_prod, braip_maps, email, senha

error = AssertionError

class TestLogin:



    def test_login_bem_sucedido(self):
        
        
        driver.get(braip_prod)
        field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
        field_login.send_keys(email)
        field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
        field_password.send_keys(senha)
        driver.save_screenshot('screen_00.png')
        field_password.send_keys(Keys.RETURN)
        print(TestLogin.test_login_bem_sucedido)
        time.sleep(5)
        title = driver.title
        print(title)
        assert 'Braip members - Home' in title  
        # print(error)      
        time.sleep(.5)
        driver.save_screenshot('screen_01.png')
