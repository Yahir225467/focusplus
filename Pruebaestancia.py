from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Proporciona la ruta del chromedriver directamente durante la creación del WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('C:/Users/LENOVO/.katalon/packages/Katalon_Studio_Windows_64-9.0.0/Katalon_Studio_Windows_64-9.0.0/configuration/resources/drivers/chromedriver_win32')

driver = webdriver.Chrome(options=chrome_options)

# Abre la página de registro
driver.get('file:///C:/Users/LENOVO/OneDrive/Escritorio/focusplus-main/assets/register.html')

# Completa el formulario
nombre_input = driver.find_element('id', 'nombre')
nombre_input.send_keys('Julio')

apellidos_input = driver.find_element('id', 'apellidos')
apellidos_input.send_keys('García Reyes')

email_input = driver.find_element('id', 'exampleInputEmail1')
email_input.send_keys('jcgr190203@micorreo.upp.edu.mx')

password_input = driver.find_element('id', 'exampleInputPassword1')
password_input.send_keys('123456789')

# Selecciona la casilla de verificación
checkbox = driver.find_element('id', 'exampleCheck1')
checkbox.click()

# Espera unos segundos para que puedas ver lo que está sucediendo (opcional)
time.sleep(3)

# Hace clic en el botón de registro
registrar_boton = driver.find_element('xpath', '//button[text()="Registrar"]')
registrar_boton.click()

# Espera unos segundos para que puedas ver el resultado (opcional)
time.sleep(3)

# Cierra el navegador al finalizar las pruebas
driver.quit()
