import pytest
from selenium import webdriver
from utils import login
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(): # Inicializa el navegador y en modo incognito para evitar problemas durante la ejecución de las pruebas.
    chrome_opt = Options()
    chrome_opt.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_opt)
    yield driver 
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver