from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from setup_login import driver, braip_prod, braip_maps, email_incorreto, senha, email_invalido, email_inexistente, email, senha_inexistente, senha_incorreta
import unittest

class LoginTestFail(unittest.TestCase):
        

    def test_login_mau_sucedido_email_incorreto(self):
        max_attempts = 5
        attempts = 0
        error_message = "E-mail informado não encontrado."
    
        while attempts < max_attempts:
            driver.get(braip_prod)
            time.sleep(1)
            field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
            field_login.send_keys(email_incorreto)
            field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
            field_password.send_keys(senha)
            field_password.send_keys(Keys.RETURN)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, braip_maps["buttons"]["erro_email"]["xpath"]))
                )
                field_error = driver.find_element(By.XPATH, braip_maps["buttons"]["erro_email"]["xpath"])
                self.assertEqual(error_message, field_error.text)
                driver.save_screenshot('screen_02.png')
                print(field_error.text)
                break
            except:
                attempts += 1
                if attempts == max_attempts:
                    raise


    def test_login_mau_sucedido_email_invalido(self):
        max_attempts = 5
        attempts = 0
        error_message = "O e-mail informado é inválido."
        
        while attempts < max_attempts:
            driver.get(braip_prod)
            # time.sleep(1)
            field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
            field_login.send_keys(email_invalido)
            field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
            field_password.send_keys(senha)
            field_password.send_keys(Keys.RETURN)

            try:
                time.sleep(.5)
                field_error = driver.find_element(By.XPATH, braip_maps["buttons"]["erro_email"]["xpath"])
                self.assertEqual(error_message, field_error.text)
                driver.save_screenshot('screen_03.png')
                print(field_error.text)
                break
            except:
                attempts += 1
                if attempts == max_attempts:
                    raise


    def test_login_mau_sucedido_email_inexistente(self):
        max_attempts = 5
        attempts = 0
        error_message = "O campo é obrigatório."
        
        while attempts < max_attempts:
            driver.get(braip_prod)
            field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
            field_login.send_keys(email_inexistente)
            field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
            field_password.send_keys(senha)
            field_password.send_keys(Keys.RETURN)

            try:
                time.sleep(1)
                field_error = driver.find_element(By.XPATH,braip_maps["buttons"]["erro_email"]["xpath"])
                self.assertEqual(error_message, field_error.text)
                driver.save_screenshot('screen_04.png')
                print(field_error.text)
                break
            except:
                attempts += 1
                if attempts == max_attempts:
                    raise


    def test_mau_sucedido_login_senha_incorreta(self):
        max_attempts = 5
        attempts = 0
        error_message = 'E-mail ou senha informados estão incorretos.'
        
        while attempts < max_attempts:
            driver.get(braip_prod)
            field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
            field_login.send_keys(email)
            field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
            field_password.send_keys(senha_incorreta)
            field_password.send_keys(Keys.RETURN)

            try:
                time.sleep(1)
                field_error = driver.find_element(By.XPATH,braip_maps["buttons"]["erro_email"]["xpath"])
                self.assertEqual(error_message, field_error.text)
                driver.save_screenshot('screen_05.png')
                print(field_error.text)
                break
            except:
                attempts +=1
                if attempts == max_attempts:
                    raise


    def test_mau_sucedido_login_senha_inexistente(self):
        max_attempts = 5
        attempts = 0
        error_message = 'O campo é obrigatório.'
        
        while attempts < max_attempts:
            driver.get(braip_prod)
            field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
            field_login.send_keys(email)
            field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
            field_password.send_keys(senha_inexistente)
            field_password.send_keys(Keys.RETURN)

            try:
                time.sleep(1)
                field_error = driver.find_element(By.XPATH,braip_maps["buttons"]["erro_senha"]["xpath"])
                self.assertEqual(error_message, field_error.text)
                driver.save_screenshot('screen_06.png')
                print(field_error.text)
                break
            except:
                attempts += 1
                if attempts == max_attempts:
                    raise