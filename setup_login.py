from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
email = 'felipe.pereira@braip.com'
email_incorreto = 'felipe@braip.com'
email_invalido = 'felipe@braip'
email_inexistente = ''
senha = 'braip*963,'
senha_incorreta = 'a'
senha_inexistente = ''
braip_prod = "https://braip.braip.club/login"
braip_report = 'file:///home/braip/Documentos/test_auto/report.html'
braip_maps = {
    "buttons": {
        "send_email": {
            "xpath": "/html/body/div[1]/div/div/main/div/div[2]/form/div[1]/div[1]/div[1]/div/input"
        },
        "send_senha": {
            "xpath": "/html/body/div[1]/div/div/main/div/div[2]/form/div[1]/div[1]/div[2]/div/div/input"
        },
        "erro_email": {
            "xpath": "/html/body/div[1]/div/div/main/div/div[2]/form/div[1]/div[1]/div[1]/div[2]/ul/li"
        },
        "erro_senha": {
            "xpath": "/html/body/div[1]/div/div/main/div/div[2]/form/div[1]/div[1]/div[2]/div[2]/ul/li"
        }
    }
}