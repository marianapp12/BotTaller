#importaciones de librerias
from selenium import webdriver #controla el navegador
from selenium.webdriver.chrome.service import Service #importamos el servicio de chrome permite manipular a chrome
from selenium.webdriver.common.by import By #acceder a varias partes
from selenium.webdriver.common.action_chains import ActionChains #varias acciones en cadena doble click
import time #altos en segundos
from selenium.webdriver.common.keys import Keys

Service =Service("./chromedriver.exe") #ruta del driver
bot_Taller = webdriver.Chrome(service=Service)#inciciar el bot
bot_Taller.maximize_window()#abra chrome abra la pestalla completa

try:
    # Abrir la página web
    bot_Taller.get("https://www.viajesexito.com")
    time.sleep(0.5)

    # Seleccionar la opción "Vuelo + Hotel"
    flight_hotel = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]')
    time.sleep(1) #tiempo de espera
    flight_hotel.click()
    time.sleep(0.5)

    # Ingresar lugar de origen busquedad
    place_origin = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
    time.sleep(0.5)#tiempo de espera
    place_origin.click()
    time.sleep(0.5)

    # Eliminar anuncio
    advertisement = bot_Taller.find_element(By.XPATH, '/html/body/div[6]/div/div')
    bot_Taller.execute_script("advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);", advertisement)
    time.sleep(3)

    # Ingresa el texto del lugar de origen
    enter_source_text = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
    time.sleep(0.5)#tiempo de espera
    enter_source_text.send_keys('José María Cordova') #texto
    time.sleep(0.5)
    enter_source_text.send_keys(Keys.ENTER)
    time.sleep(0.5)

    # Ingresar lugar de destino busquedad
    destination_place = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
    time.sleep(1)#tiempo de espera
    destination_place.click()
    time.sleep(1)

    # Ingresar el texto del lugar de destino
    destination_place_enter = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
    time.sleep(0.5)#tiempo de espera
    destination_place_enter.send_keys('cun-aeropuerto internacional')
    time.sleep(3)#tiempo de espera
    destination_place_enter.send_keys(Keys.ARROW_DOWN)#flecha hacia abajo y selecciona
    destination_place_enter.send_keys(Keys.ENTER)#enter

    # Mostrar el calendario
    calendar_sample = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
    time.sleep(2)#tiempo de espera
    calendar_sample.click()#clic en el calendario
    time.sleep(2)

    # Seleccionar fecha de salida
    departure_date = bot_Taller.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[2]/div[2]/div[1]')
    departure_date.click()
    time.sleep(1)

    # Seleccionar fecha de llegada
    arrival_date = bot_Taller.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[6]/div[2]/div[1]')
    arrival_date.click()
    time.sleep(3)

    # Simular teclas pulsacion
    bot_Taller.execute_script("""
        var tap = new KeyboardEvent('keydown', {bubbles: true, cancelable: true, keyCode: 9});
        document.dispatchEvent(tap);
    """)

    #simula la tecla de enter
    bot_Taller.execute_script("""
        var enter = new KeyboardEvent('keydown', {bubbles: true, cancelable: true, keyCode: 13});
        document.dispatchEvent(enter);
    """)
    time.sleep(2)

    # adultos que viajan habitacion numero 1 
    adults_N2_room_1 = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p')
    adults_N2_room_1.click()#1 dos personas 
    time.sleep(2)

    #selecciona agregar habitacion
    room_2 = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
    room_2.click()
    time.sleep(2)

    #adultos que viajan habitacion 2
    adults_N3_room_2 = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/div/span[2]/button/span')
    adults_N3_room_2.click()#2 personas
    adults_N3_room_2.click()#3 personas
    time.sleep(2)

    #boton de aplicar de habitaciones y huespedes
    apply_button = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
    apply_button.click()
    time.sleep(2)

    # Realizar búsqueda
    search = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a/p')
    search.click() #clic en buscar
    time.sleep(15)

    # Cambiar a la nueva ventana
    window_handles = bot_Taller.window_handles
    bot_Taller.switch_to.window(window_handles[-1])
    time.sleep(1)

    # Obtener precios y mostrar en la consola f: pyhton una cadena texto 
    for i in range(10):
        price = bot_Taller.find_element(By.XPATH,f'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[{i+1}]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
        print("The price is:" + price.text)
    time.sleep(5)

    # Configuración avanzada
    advanced_config = bot_Taller.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
    advanced_config.click()#click
    time.sleep(2)

    # Seleccionar aerolínea
    new_airline = bot_Taller.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
    new_airline.click()#click
    time.sleep(1)#tiempo de espera
    new_airline.send_keys('kor')#texto que se introduce
    time.sleep(1)
    new_airline.send_keys(Keys.ENTER)#enter
    time.sleep(1)

    # Busca la nueva aerolinea
    search = bot_Taller.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
    search.click()
    time.sleep(10)

    # Desplazar la página hacia abajo
    bot_Taller.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    # Hacer clic en WhatsApp
    wsp = bot_Taller.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p[1]/a')
    wsp.click()#click
    time.sleep(2)

finally:
    # Cerrar el navegador
    bot_Taller.quit()