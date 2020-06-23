from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

#GUARDA LA SESION DEL USUARIO
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=./User_Data')

#CARGA EL NAVEGADOR Y ABRE LA PAGINA
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://web.whatsapp.com/')
timeout = 30

try:
    #VERIFICA QUE ESTE LOGEADO
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[4]/div/div/div[2]/h1'))
    WebDriverWait(driver, timeout).until(element_present)
    print('LOGEADO EXITOSAMENTE.')

except TimeoutException:
    print('ESCANEA EL CODIGO QR Y PRECIONA ENTER:')
    input()
    print('CARGANDO MENU........')

def enviar_mensaje(contacto,mensaje):
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(contacto)
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(mensaje)
    msg_box.send_keys(Keys.ENTER)
    print('MENSAJE ENVIADO A ' + contacto)
    time.sleep(3)


def wellcome():
    print('BIENVENIDO')
    print('1-) ENVIAR MENSAJE')
    print('2-) MENSAJE MASIVO')
    print('3-) SALIR')

salir = True

wellcome()
while salir:
    option = input("INGRESE UNA OPCION: ")
    if option == '1':
        contacto = input('INGRESE CONTACTO: ')
        mensaje = input('INGRESE MENSAJE: ')
        enviar_mensaje(contacto,mensaje)
    if option == '2':
        mensaje = input('INGRESE MENSAJE: ')
        cantidad = int(input('A CUANTAS PERSONAS DESEA MANDAR EL MENSAJE: '))
        contactos = []
        for x in range(cantidad):
                contacto = input('INGRESE CONTACTO ' + str(x+1) + ':')
                contactos.append(contacto)
        for contacto in contactos:
             enviar_mensaje(contacto,mensaje)

        print('MENSAJES ENVIADOS CON EXITO')
    elif option == '3':
        print('ADIOS......')
        driver.quit()
        salir = False
