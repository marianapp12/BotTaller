#library imports
from selenium import webdriver #control the browser
from selenium.webdriver.chrome.service import Service #we import the chrome service allows to manipulate chrome
from selenium.webdriver.common.by import By #access multiple parts
from selenium.webdriver.common.action_chains import ActionChains #varias acciones en cadena doble click
import time #high in seconds
from selenium.webdriver.common.keys import Keys

Service =Service("./chromedriver.exe")#driver path
bot_Taller = webdriver.Chrome(service=Service)#start the bot
bot_Taller.maximize_window()#open chrome open full tab

try:
    # Open the web page
    bot_Taller.get("https://www.viajesexito.com")
    time.sleep(0.5)

    # Select the "Flight + Hotel" option
    flight_hotel = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]')
    time.sleep(1) #wait time
    flight_hotel.click()
    time.sleep(0.5)

    # Enter place of origin search
    place_origin = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
    time.sleep(0.5)#wait time
    place_origin.click()
    time.sleep(0.5)

    # Remove ad
    advertisement = bot_Taller.find_element(By.XPATH, '/html/body/div[6]/div/div')
    bot_Taller.execute_script("advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);", advertisement)
    time.sleep(3)

    # Enter the text of the place of origin
    enter_source_text = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
    time.sleep(0.5)#wait time
    enter_source_text.send_keys('José María Cordova') #texto
    time.sleep(0.5)
    enter_source_text.send_keys(Keys.ENTER)
    time.sleep(0.5)

   # Enter destination search location
    destination_place = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
    time.sleep(1)#wait time
    destination_place.click()
    time.sleep(1)

    # Enter the text of the destination place
    destination_place_enter = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
    time.sleep(0.5)#wait time
    destination_place_enter.send_keys('cun-aeropuerto internacional')
    time.sleep(3)#wait time
    destination_place_enter.send_keys(Keys.ARROW_DOWN)#down arrow and select
    destination_place_enter.send_keys(Keys.ENTER)#enter

    # Show calendar
    calendar_sample = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
    time.sleep(2)#wait time
    calendar_sample.click()#click on the calendar
    time.sleep(2)

    # Select departure date
    departure_date = bot_Taller.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[6]/div[2]/div[2]/div[1]')
    departure_date.click()
    time.sleep(1)

    # Select arrival date
    arrival_date = bot_Taller.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[6]/div[2]/div[1]')
    arrival_date.click()
    time.sleep(3)#wait time

    # Simulate keystrokes
    bot_Taller.execute_script("""
        var tap = new KeyboardEvent('keydown', {bubbles: true, cancelable: true, keyCode: 9});
        document.dispatchEvent(tap);
    """)

   #simulates the enter key
    bot_Taller.execute_script("""
        var enter = new KeyboardEvent('keydown', {bubbles: true, cancelable: true, keyCode: 13});
        document.dispatchEvent(enter);
    """)
    time.sleep(2)#wait time

    # adults traveling room number 1
    adults_N2_room_1 = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p')
    adults_N2_room_1.click()#1 dos personas 
    time.sleep(2)#wait time

    #select add room
    room_2 = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
    room_2.click()
    time.sleep(2)#wait time

    #adults traveling room 2
    adults_N3_room_2 = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/div/span[2]/button/span')
    doubleclickaction = ActionChains(bot_Taller)#double click action
    doubleclickaction.double_click(adults_N3_room_2).perform()#double click to add two adults
    time.sleep(2)#wait time

    #apply button for rooms and guests
    apply_button = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
    apply_button.click()#click
    time.sleep(2)#wait time

    # Perform search
    search = bot_Taller.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a/p')
    search.click() #click on search
    time.sleep(15)#wait time

    # Switch to new window
    window_handles = bot_Taller.window_handles
    bot_Taller.switch_to.window(window_handles[-1])
    time.sleep(1)#wait time

    # Get prices and display in the console: python a text string
    for i in range(10):
        price = bot_Taller.find_element(By.XPATH,f'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[{i+1}]/div/div/div[2]/div/div[1]/div/p[1]/span[2]')
        print("The price is:" + price.text)
    time.sleep(5)#wait time

    # Configuración avanzada
    advanced_config = bot_Taller.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
    advanced_config.click()#click
    time.sleep(2)#wait time

    # Select airline
    new_airline = bot_Taller.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
    new_airline.click()#click
    time.sleep(1)#wait time
    new_airline.send_keys('kor')#text to be entered
    time.sleep(1)#wait time
    new_airline.send_keys(Keys.ENTER)#enter
    time.sleep(1)#wait time

    # Find the new airline
    search = bot_Taller.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
    search.click()
    time.sleep(10)#wait time

    # Scroll page down
    bot_Taller.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)#wait time

    # Hacer clic en WhatsApp
    wsp = bot_Taller.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p[1]/a')
    wsp.click()#click
    time.sleep(2)#wait time

finally:
    # Close the browser
    bot_Taller.quit()