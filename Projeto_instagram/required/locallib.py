# Inteiramente Desenvolvido Por: Luan Carlos Soares Pereira

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
url = "https://www.instagram.com/"

now = datetime.now()
expired = datetime.strptime('25/05/2021 23:59:59', "%d/%m/%Y %H:%M:%S")
tod = str(f'{now.day}{now.month}{now.year}') + ' ' + str(now.hour)+ '' + str(now.minute)

def caption(caption):
    arquivo = open(f'{caption}', 'r')
    legenda = arquivo.read()
    return legenda

def transform_mobile():
    pyautogui.hotkey('ctrl','shift','i')
    time.sleep(1)
    pyautogui.hotkey('ctrl','shift','m')
    time.sleep(1)

def upload_photo_video(path):
    legenda = caption(f'{path}/d1.txt')

    pyautogui.click('Buttons//postar.png')
    time.sleep(2)
    pyautogui.write(f'{path}')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('f1.jpg')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click('Buttons//Next.png')
    time.sleep(1)
    pyautogui.click('Buttons//Write.png')
    time.sleep(1)
    pyautogui.write(f'{legenda}')
    time.sleep(1)
    pyautogui.click('Buttons//Share.png')

def post(user, password, path):
    if now <= expired:
        driver = webdriver.Chrome(executable_path=r'./required/chromedriver.exe')
        driver.get(url)
        time.sleep(2)

        driver.find_element(By.NAME, "username").send_keys(f'{user}' + Keys.TAB)
        driver.find_element(By.NAME, "password").send_keys(f'{password}' + Keys.ENTER)
        time.sleep(3)

        driver.get(f'{url}{user}')

        transform_mobile()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)

        upload_photo_video(path)
        time.sleep(5)
        #driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/button[1]/span').click()
        time.sleep(10)
        driver.quit()
    else:
        print(f'Licença Expirada Dia: {expired}')

        
