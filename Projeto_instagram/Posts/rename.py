import os
import time
import shutil
from datetime import datetime

now = datetime.now()
tod = str(f'{now.day}{now.month}{now.year}') + ' ' + str(now.hour)+ '' + str(now.minute)

def switch():
    for item in os.listdir():
        if f'f1' in item:
            os.rename(item, f'Foto Postada {tod}.jpg')
        if f'd1' in item:
            os.rename(item, f'Descricao Postada {tod}.txt')

def ordem():
    c = 1
    for c in range(len(os.listdir())):
        for item in os.listdir():
            if f'f{c}' in item:
                novof = f'f{c-1}.jpg'
                os.rename(item, novof)
            if f'd{c}' in item:
                novod = f'd{c-1}.txt'
                os.rename(item, novod)

def mv():
    for item in os.listdir():
        if 'Postada' in item:
            shutil.move(f'{item}','D:\Projeto_instagram\Posts\Postadas')

switch()
time.sleep(2)
mv()
time.sleep(2)
ordem()
