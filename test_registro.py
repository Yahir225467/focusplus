import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
    # Proporciona la ruta del chromedriver directamente durante la creación del WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('C:/Users/LENOVO/.katalon/packages/Katalon_Studio_Windows_64-9.0.0/Katalon_Studio_Windows_64-9.0.0/configuration/resources/drivers/chromedriver_win32')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_registro_exitoso(browser):
    browser.get('file:///C:/Users/LENOVO/OneDrive/Escritorio/focusplus-main/assets/register.html')

    # Completa el formulario
    nombre_input = browser.find_element('id', 'nombre')
    nombre_input.send_keys('Julio Cesar')

    apellidos_input = browser.find_element('id', 'apellidos')
    apellidos_input.send_keys('Garcia Reyes)

    email_input = browser.find_element('id', 'exampleInputEmail1')
    email_input.send_keys('jcgr190203@micorreo.upp.edu.mx')

    password_input = browser.find_element('id', 'exampleInputPassword1')
    password_input.send_keys('123456789')

    # Selecciona la casilla de verificación
    checkbox = browser.find_element('id', 'exampleCheck1')
    checkbox.click()

    # Espera unos segundos para que puedas ver lo que está sucediendo (opcional)
    time.sleep(3)

    # Hace clic en el botón de registro
    registrar_boton = browser.find_element('xpath', '//button[text()="Registrar"]')
    registrar_boton.click()

    # Espera unos segundos para que puedas ver el resultado (opcional)
    time.sleep(3)

    # Verifica el resultado (esto es solo un ejemplo, puedes ajustarlo según tus necesidades)
    assert "Registro exitoso" in browser.page_source
