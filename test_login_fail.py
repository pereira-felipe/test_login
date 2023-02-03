from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from setup_login import driver, braip_prod, braip_maps, email_incorreto, senha, email_invalido, email_inexistente, email, senha_inexistente, senha_incorreta


class TestLoginFail:


    def test_login_mau_sucedido_email_incorreto(self):

        driver.get(braip_prod)
        time.sleep(1)
        field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
        field_login.send_keys(email_incorreto)
        field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
        field_password.send_keys(senha)
        field_password.send_keys(Keys.RETURN)
        time.sleep(1)
        field_error = driver.find_element(By.XPATH,braip_maps["buttons"]["erro_email"]["xpath"])
        print(field_error.text)
        assert 'E-mail informado não encontrado.' in field_error.text
        time.sleep(1)
        driver.save_screenshot('screen_02.png')


    def test_login_mau_sucedido_email_invalido(self):

        driver.get(braip_prod)
        field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
        field_login.send_keys(email_invalido)
        field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
        field_password.send_keys(senha)
        field_password.send_keys(Keys.RETURN)
        time.sleep(1)
        field_error = driver.find_element(By.XPATH,braip_maps["buttons"]["erro_email"]["xpath"])
        print(field_error.text)
        assert 'O e-mail informado é inválido.' in field_error.text
        time.sleep(1)
        driver.save_screenshot('screen_03.png')


    def test_login_mau_sucedido_email_inexistente(self):

        driver.get(braip_prod)
        field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
        field_login.send_keys(email_inexistente)
        field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
        field_password.send_keys(senha)
        field_password.send_keys(Keys.RETURN)
        time.sleep(1)
        field_error = driver.find_element(By.XPATH,braip_maps["buttons"]["erro_email"]["xpath"])
        print(field_error.text)
        assert 'O campo é obrigatório.' in field_error.text
        time.sleep(1)
        driver.save_screenshot('screen_04.png')


    def test_mau_sucedido_login_senha_incorreta(self):

        driver.get(braip_prod)
        field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
        field_login.send_keys(email)
        field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
        field_password.send_keys(senha_incorreta)
        field_password.send_keys(Keys.RETURN)
        time.sleep(1)
        field_error = driver.find_element(By.XPATH,braip_maps["buttons"]["erro_email"]["xpath"])
        print(field_error.text)
        assert 'E-mail ou senha informados estão incorretos.' in field_error.text
        time.sleep(1)
        driver.save_screenshot('screen_05.png')


    def test_mau_sucedido_login_senha_inexistente(self):

        driver.get(braip_prod)
        field_login = driver.find_element(By.XPATH,braip_maps["buttons"]["send_email"]["xpath"])
        field_login.send_keys(email)
        field_password = driver.find_element(By.XPATH,braip_maps["buttons"]["send_senha"]["xpath"])
        field_password.send_keys(senha_inexistente)
        field_password.send_keys(Keys.RETURN)
        time.sleep(1)
        field_error = driver.find_element(By.XPATH,braip_maps["buttons"]["erro_senha"]["xpath"])
        print(field_error.text)
        assert 'O campo é obrigatório.' in field_error.text
        time.sleep(1)
        driver.save_screenshot('screen_06.png')


    def teardown_class(self):
        time.sleep(1)
        driver.close()