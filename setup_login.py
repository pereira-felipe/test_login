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
            "xpath": "/html/body/div[1]/div/div/main/div/div[2]/form/div[1]/div[1]/div[1]/div[2]"
        },
        "erro_senha": {
            "xpath": "/html/body/div[1]/div/div/main/div/div[2]/form/div[1]/div[1]/div[2]/div[2]/ul/li"
        },
        "send_like": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[2]/div/section/div[2]/div/div[2]/span/div[1]"
        },
        "send_search": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[1]/div/div"
        },
        "send_search_key": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[1]/div/div[1]/input"
        },
        "send_favorites": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[2]/a/div"
        },
        "home": {
            "xpath": "/html/body/div[1]/div/div/main/section/div[1]/div/div/div/a/div/img"
        },
        "notification": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[3]/div/button/div/div"
        },
        "selection": {
            "xpath": "/html/body/div[1]/div/div/main/section/div[2]/div/div/div[1]/div[1]/div/div/details/summary"
        },
        "antigos": {
            "xpath": "/html/body/div[1]/div/div/main/section/div[2]/div/div/div[1]/div[1]/div/div/details/ul/li[2]/label"
        },
        "recentes": {
            "xpath": "/html/body/div[1]/div/div/main/section/div[2]/div/div/div[1]/div[1]/div/div/details/ul/li[1]/label"
        },
        "aula": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[2]/div/div/div[1]/section/div[2]/div[1]/div/div/div[1]"
        },
        "perfil": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[4]/div/button/div/div[1]/img"
        },
        "logout": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[4]/div/div/div[2]/div/div[6]/div"
        },
        "profile_account": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[4]/div/div/div[2]/div/div[1]/div[1]"
        },
        "progress": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[2]/div/div/div[2]/section/div[1]"
        },
        "account": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[4]/div/div/div[2]/div/div[2]/div[1]"
        },
        "close": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[4]/div/div/div[1]/div[2]/button/div/i"
        },
        "support": {
            "xpath": "/html/body/div[1]/div/div/main/div[2]/section/div[1]/div/div/ul/li[4]/div/div/div[2]/div/div[4]/div[1]"
        }
    }
}