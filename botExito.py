#importaciones de librerias
from selenium import webdriver #controla el navegador
from selenium.webdriver.chrome.service import Service #importamos el servicio de chrome permite manipular a chrome
from selenium.webdriver.common.by import By #acceder a varias partes
from selenium.webdriver.common.action_chains import ActionChains #varias acciones en cadena doble click
import time #altos en segundos
from selenium.webdriver.common.keys import Keys

Service =Service("botTaller/chromedriver.exe") #ruta del driver
bot_Taller = webdriver.Chrome(service=Service)#inciciar el bot
bot_Taller.maximize_window()#abra chrome abra la pestalla completa

bot_Taller.get("https://www.viajesexito.com")#lleve a una pagina web entre a ("dirreccion web")
time.sleep(0.5)#espera 3 segundos ventana abierta

#vuelo+hotel
vuelo_hotel= bot_Taller.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]')
time.sleep(1)
vuelo_hotel.click()
time.sleep(0.5)

#origen busquedad
lugar_origen = bot_Taller.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
time.sleep(0.5)
lugar_origen.click()
time.sleep(0.5)

#eliminar el anuncio
anuncio = bot_Taller.find_element(By.XPATH,'/html/body/div[6]/div/div')
bot_Taller.execute_script("anuncio = arguments[0];anuncio.parentNode.removeChild(anuncio);", anuncio)
time.sleep(3)

#texto de origen
texto_origen_enter = bot_Taller.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
time.sleep(0.5)
texto_origen_enter.send_keys('José María Cordova')
time.sleep(0.5)
texto_origen_enter.send_keys(Keys.ENTER)
time.sleep(0.5)

#lugar de destino
lugar_destino = bot_Taller.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
time.sleep(1)
lugar_destino.click()
time.sleep(1)

#texto de destino aun no da
lugar_destino_enter = bot_Taller.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
time.sleep(2)
lugar_destino_enter.send_keys('Cancun')
time.sleep(2)
bot_Taller.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
time.sleep(2)
lugar_destino_enter.send_keys(Keys.ENTER)
time.sleep(2)

#muestra el calendario
muestra_calendario = bot_Taller.find_element(By.XPATH,'/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
time.sleep(2)
muestra_calendario.click()
time.sleep(2)

