import json
import sys

Author = '''
    
██████╗░██╗░░░██╗██╗  ░██╗░░░░░░░██╗░█████╗░██╗░░░██╗██████╗░██╗░░██╗
██╔══██╗╚██╗░██╔╝╚═╝  ░██║░░██╗░░██║██╔══██╗╚██╗░██╔╝██╔══██╗██║░██╔╝
██████╦╝░╚████╔╝░░░░  ░╚██╗████╗██╔╝██║░░██║░╚████╔╝░██████╔╝█████═╝░
██╔══██╗░░╚██╔╝░░░░░  ░░████╔═████║░██║░░██║░░╚██╔╝░░██╔══██╗██╔═██╗░
██████╦╝░░░██║░░░██╗  ░░╚██╔╝░╚██╔╝░╚█████╔╝░░░██║░░░██║░░██║██║░╚██╗
╚═════╝░░░░╚═╝░░░╚═╝  ░░░╚═╝░░░╚═╝░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝

'''

import argparse
from json import load, dump
from sys import exit, stdout, stderr
from os import getcwd
from subprocess import run
from shutil import move
import textwrap

OP = """
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓███████▓▓█▓▓███████▓▓▓▓▓▓▓▓▓▓▓▓█
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓ 
    ▓█▓█████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▓▓▓▓██
    ▓█▓███████▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▓░░░░▒█
    ▓█▓██████▓█▓█▓▒█▒▒▓▒▒▒▒▒▒▒▓▒▒▒▒▒▒▓██▓▒▒░▒▓█
    ▓█▓██████▓▓▓▓▒▓▓█▒▓▒▓▒▒▒█▒▓▒▒█▒▒▒▒███▓▒▒▒██
    ▓▓▓███████▓▓▓▓▒▒▓▓▓█▒▒▒▓█░▒▓█▒▒▒▒▒████▒▒▓██
    ▓▓▓███████▓▓▓▓▒▒▒▒▒██▓▓▒▒▒▒▒█▓▒▓███▒░░░▒▒░░
    ▓▓▓███████▓▓▓▓▓▒█░░░░░░░██▒█▓▒▒▓█▓▒▓▓▓▒▓▓▒▓
    ▓▓▓████████▓▓▓▓█░░░░░░░░░░░▓▓▓▒▓▓▒░▒▓▓▓▒▓▒▓
    ▓▓▓███████░░▓▓▓▓▓░░░▒░░░░░░▓▒█░░░░░▒▒▓▓▒▒▓▓
    ▓▓▓█████▓▓▓░░▓▓▓▓▒░░░▒░░░░░██▒▓░░▓▓▓▓▓▓▒░▒▓ 
    ▓▓▓▓▓▓░▓▓▓▓░░░░░░░█░░░░░░▒░░░░░░▓▓▓▓░░▓▓▒▒▒
    ▓▓▓▓▓░░░▓▓░░░░░░░░░░░░░░▓░░░░░░░░▓▒░░░░█▒▒▒
    ▓▓▓▓░░█░░░░░░▒▓█▒▒▒▒░░░░░▒▒▒▒▒░░░░░░░░░░▓▓▓
    ▓▓▓░░░░░▒░░░▒▓▓▓▓░▓▒█▒░░█▒░▓▓▓▓░░░░░░▒░░░▓▓
    ▓▓▓░░░░█░░░░▓▓▓▓▓▓░█▓██▓█░░▓▓▓▓▓░░░░░▒░░░█▓
    ▓▓░░░░░░░░░▓▓▓▓▓▓██▓█▓█▒░▓▓▓▓▓▓▓░░░░░▒░░░░▓
    ▒░░░░░░░░░░▓▓▓▓▓▓▓▓▒█▒█▒░░▓▓▓▓▓▓▓░░░░░▒░░░░
    ▒░░░░░░░░░▓▓▓▓▓▓▓▓▓▓█▒▓█░░▓▓▓▓▓▓▓▓░░░░░█░░░
    ░░░░░░░░░░░░█▓▓▓▓▓▓▓█▒▒▒▒▓▓▓▓▓▓▓▓▒░░░░░░░░░ 
"""

OP1 = '''
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                                      
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
    LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL 
'''

DataSend = {
    'Image': OP,
    
    'SendToday': False,
    'PROFILE': None,
    'PROFILEMOVE': None,
    'UsesImageFile': None,
    'Uses': False,
    'UsesTwo': False,
    'UsesThree': False,
    'UserLaing': None,
    'SelectImageFromUser': None,
}

IMAGEFROMUSER = None

print(f'{Author}\nЗапущена версия v1.1')
print('TG - t.me/alcteri')

SelLang = str(input('\nPls select language: (Rus or Eng)'))

if SelLang == 'Rus':
    with open('TempData.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        sys.stderr.write('\nПроверка')
        if not data['Uses'] == True:
            data['Uses'] = True
            sys.stderr.write('\nЗапись....')

            with open('TempData.json', 'w', encoding='utf-8') as f2:
                json.dump(data, f2, ensure_ascii=False, indent=4)

            with open('data.json', 'w', encoding='utf-8') as f1:

                sys.stderr.write('''\n
                    1)                                              
                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     
                    ▓▓▓▓▓▓▓▓▓▓▓███████▓▓█▓▓███████▓▓▓▓▓▓▓▓▓▓▓▓█
                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓ 
                    ▓█▓█████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▓▓▓▓██
                    ▓█▓███████▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▓░░░░▒█
                    ▓█▓██████▓█▓█▓▒█▒▒▓▒▒▒▒▒▒▒▓▒▒▒▒▒▒▓██▓▒▒░▒▓█
                    ▓█▓██████▓▓▓▓▒▓▓█▒▓▒▓▒▒▒█▒▓▒▒█▒▒▒▒███▓▒▒▒██
                    ▓▓▓███████▓▓▓▓▒▒▓▓▓█▒▒▒▓█░▒▓█▒▒▒▒▒████▒▒▓██
                    ▓▓▓███████▓▓▓▓▒▒▒▒▒██▓▓▒▒▒▒▒█▓▒▓███▒░░░▒▒░░
                    ▓▓▓███████▓▓▓▓▓▒█░░░░░░░██▒█▓▒▒▓█▓▒▓▓▓▒▓▓▒▓
                    ▓▓▓████████▓▓▓▓█░░░░░░░░░░░▓▓▓▒▓▓▒░▒▓▓▓▒▓▒▓
                    ▓▓▓███████░░▓▓▓▓▓░░░▒░░░░░░▓▒█░░░░░▒▒▓▓▒▒▓▓
                    ▓▓▓█████▓▓▓░░▓▓▓▓▒░░░▒░░░░░██▒▓░░▓▓▓▓▓▓▒░▒▓ 
                    ▓▓▓▓▓▓░▓▓▓▓░░░░░░░█░░░░░░▒░░░░░░▓▓▓▓░░▓▓▒▒▒
                    ▓▓▓▓▓░░░▓▓░░░░░░░░░░░░░░▓░░░░░░░░▓▒░░░░█▒▒▒
                    ▓▓▓▓░░█░░░░░░▒▓█▒▒▒▒░░░░░▒▒▒▒▒░░░░░░░░░░▓▓▓
                    ▓▓▓░░░░░▒░░░▒▓▓▓▓░▓▒█▒░░█▒░▓▓▓▓░░░░░░▒░░░▓▓
                    ▓▓▓░░░░█░░░░▓▓▓▓▓▓░█▓██▓█░░▓▓▓▓▓░░░░░▒░░░█▓
                    ▓▓░░░░░░░░░▓▓▓▓▓▓██▓█▓█▒░▓▓▓▓▓▓▓░░░░░▒░░░░▓
                    ▒░░░░░░░░░░▓▓▓▓▓▓▓▓▒█▒█▒░░▓▓▓▓▓▓▓░░░░░▒░░░░
                    ▒░░░░░░░░░▓▓▓▓▓▓▓▓▓▓█▒▓█░░▓▓▓▓▓▓▓▓░░░░░█░░░
                    ░░░░░░░░░░░░█▓▓▓▓▓▓▓█▒▒▒▒▓▓▓▓▓▓▓▓▒░░░░░░░░░
                ''')

                sys.stderr.write('''\n
                2)                                            
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        

                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL   
                ''')

                a = int(input('Pls select image for terminal(1 or 2 .....)\n'))
                DataSend['SelectImageFromUser'] = a

                if a == 1:
                    DataSend['Image'] = OP
                else:
                    DataSend['Image'] = OP1

                data2 = DataSend
                json.dump(data2, f1, ensure_ascii=False, indent=4)
                sys.stderr.write('\nУспешно')

        else:
            pass

    with open('data.json', 'r+', encoding='utf-8') as f:
        data = load(f)

        if not data['UsesTwo'] == True:
            stderr.write('\nСейчас вам потребуется пройти всн по инскрутции')
            stderr.write('\n-----------------------------------')
            command2 = 'Write-Host $PROFILE -ForegroundColor Cyan'
            run(["powershell.exe", "-Command", command2])
            a = input('Путь которой вам сейчас выдало надо скопировать и вести')

            b = input(r'Ведите путь без НазваниеФайла.ps1(Пример - C:\Users\lesha\Documents\WindowsPowerShell\)')

            stderr.write('\nПуть получен запись его в джсон файл...')
            stderr.write('\n0/5')
            data['UsesTwo'] = True
            stderr.write('\n1/5')
            data['PROFILE'] = a
            stderr.write('\n2/5')
            data['PROFILEMOVE'] = b
            stderr.write('\n3/5')

            with open('data.json', 'w', encoding='utf-8') as f3:
                dump(data, f3, ensure_ascii=False, indent=4)
                stderr.write('\n4/4')
                """
                stderr.write('\n Сейчас вам надо будет снова перезапустить скрипт, но после того перезапуска вам надо будет запускать скрипт с аргументами для настройки')
                stderr.write('''\n
                    Пример - py main.py --SendToday True start
                    py main.py (start, --SendToday)
                    В start просто пишите start
                    В --SendToday надо поставить значение False либо True         
                    ''')
                """
        else:
            pass



    PROFILE = None
    PROFILEMOVE = None
    PROFIILEBACK = None
    IMAGE = None

    USES = False

    stdout.write('\n0/2')

    with open('data.json', 'r+', encoding='utf-8') as f:
        data = load(f)

        if not data['UsesThree'] == True:
            USES = True
            with open('data.json', 'r+', encoding='utf-8') as f1:
                data1 = load(f1)

                stderr.write('\n1/2')
                PROFILE = data1['PROFILE']
                PROFILEMOVE = data1['PROFILEMOVE']
                PROFILEBACK = getcwd()
                IMAGE = data1['Image']
                move(PROFILE, PROFILEBACK)

                text = (
                    "Clear-Host\n\n"
                    "$Hellowing = @\"\n"
                    f"{IMAGE}   Hello!\n"
                    "\"@\n\n"
                    "Write-Host $Hellowing\n"
                )

                with open('Microsoft.PowerShell_profile.ps1', 'w', encoding='utf-8-sig') as f2:

                    f2.write(text)
                    stderr.write('\n2/2')
            move('Microsoft.PowerShell_profile.ps1', PROFILEMOVE)
        else:
            pass


    if USES == True:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = load(f)

            data['UsesThree'] = True
            with open ('data.json', 'w', encoding='utf-8') as f1:
                dump(data, f1, ensure_ascii=False, indent=4)
else:
    with open('TempData.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        sys.stderr.write('\nChecking')
        if not data['Uses'] == True:
            data['Uses'] = True
            sys.stderr.write('\nWriting....')

            with open('TempData.json', 'w', encoding='utf-8') as f2:
                json.dump(data, f2, ensure_ascii=False, indent=4)

            with open('data.json', 'w', encoding='utf-8') as f1:
                sys.stderr.write('''\n
                                    1)                                              
                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     
                                    ▓▓▓▓▓▓▓▓▓▓▓███████▓▓█▓▓███████▓▓▓▓▓▓▓▓▓▓▓▓█
                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓ 
                                    ▓█▓█████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▓▓▓▓██
                                    ▓█▓███████▓▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▓░░░░▒█
                                    ▓█▓██████▓█▓█▓▒█▒▒▓▒▒▒▒▒▒▒▓▒▒▒▒▒▒▓██▓▒▒░▒▓█
                                    ▓█▓██████▓▓▓▓▒▓▓█▒▓▒▓▒▒▒█▒▓▒▒█▒▒▒▒███▓▒▒▒██
                                    ▓▓▓███████▓▓▓▓▒▒▓▓▓█▒▒▒▓█░▒▓█▒▒▒▒▒████▒▒▓██
                                    ▓▓▓███████▓▓▓▓▒▒▒▒▒██▓▓▒▒▒▒▒█▓▒▓███▒░░░▒▒░░
                                    ▓▓▓███████▓▓▓▓▓▒█░░░░░░░██▒█▓▒▒▓█▓▒▓▓▓▒▓▓▒▓
                                    ▓▓▓████████▓▓▓▓█░░░░░░░░░░░▓▓▓▒▓▓▒░▒▓▓▓▒▓▒▓
                                    ▓▓▓███████░░▓▓▓▓▓░░░▒░░░░░░▓▒█░░░░░▒▒▓▓▒▒▓▓
                                    ▓▓▓█████▓▓▓░░▓▓▓▓▒░░░▒░░░░░██▒▓░░▓▓▓▓▓▓▒░▒▓ 
                                    ▓▓▓▓▓▓░▓▓▓▓░░░░░░░█░░░░░░▒░░░░░░▓▓▓▓░░▓▓▒▒▒
                                    ▓▓▓▓▓░░░▓▓░░░░░░░░░░░░░░▓░░░░░░░░▓▒░░░░█▒▒▒
                                    ▓▓▓▓░░█░░░░░░▒▓█▒▒▒▒░░░░░▒▒▒▒▒░░░░░░░░░░▓▓▓
                                    ▓▓▓░░░░░▒░░░▒▓▓▓▓░▓▒█▒░░█▒░▓▓▓▓░░░░░░▒░░░▓▓
                                    ▓▓▓░░░░█░░░░▓▓▓▓▓▓░█▓██▓█░░▓▓▓▓▓░░░░░▒░░░█▓
                                    ▓▓░░░░░░░░░▓▓▓▓▓▓██▓█▓█▒░▓▓▓▓▓▓▓░░░░░▒░░░░▓
                                    ▒░░░░░░░░░░▓▓▓▓▓▓▓▓▒█▒█▒░░▓▓▓▓▓▓▓░░░░░▒░░░░
                                    ▒░░░░░░░░░▓▓▓▓▓▓▓▓▓▓█▒▓█░░▓▓▓▓▓▓▓▓░░░░░█░░░
                                    ░░░░░░░░░░░░█▓▓▓▓▓▓▓█▒▒▒▒▓▓▓▓▓▓▓▓▒░░░░░░░░░
                                ''')

                sys.stderr.write('''\n
                                2)                                            
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        

                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL        
                                        LLLLLLLLLLLLLLLLLL  LLLLLLLLLLLLLLLLLL   
                                ''')

                a = int(input('Pls select image for terminal(1 or 2 .....)\n'))
                DataSend['SelectImageFromUser'] = a

                if a == 1:
                    DataSend['Image'] = OP
                else:
                    DataSend['Image'] = OP1


                data2 = DataSend
                json.dump(data2, f1, ensure_ascii=False, indent=4)
                sys.stderr.write('\nSuccess')
        else:
            pass

    with open('data.json', 'r+', encoding='utf-8') as f:
        data = load(f)

        if not data['UsesTwo'] == True:
            stderr.write('\nNow you need to go through VSN according to instructions')
            stderr.write('\n-----------------------------------')
            command2 = 'Write-Host $PROFILE -ForegroundColor Cyan'
            run(["powershell.exe", "-Command", command2])
            a = input('Copy the path you were just given and paste it here')

            b = input(
                r'Enter the path without the filename.ps1 (Example - C:\Users\lesha\Documents\WindowsPowerShell\)')

            stderr.write('\nPath received, writing it to JSON file...')
            stderr.write('\n0/5')
            data['UsesTwo'] = True
            stderr.write('\n1/5')
            data['PROFILE'] = a
            stderr.write('\n2/5')
            data['PROFILEMOVE'] = b
            stderr.write('\n3/5')

            with open('data.json', 'w', encoding='utf-8') as f3:
                dump(data, f3, ensure_ascii=False, indent=4)
                stderr.write('\n4/4')
                """
                stderr.write('\n Now you will need to restart the script, but after restart you need to run the script with arguments for configuration')
                stderr.write('''\n
                    Example - py main.py --SendToday True start
                    py main.py (start, --SendToday)
                    For start just write start
                    For --SendToday you need to set value False or True         
                    ''')
                """
        else:
            pass

    PROFILE = None
    PROFILEMOVE = None
    PROFIILEBACK = None
    IMAGE = None

    USES = False

    stdout.write('\n0/2')

    with open('data.json', 'r+', encoding='utf-8') as f:
        data = load(f)

        if not data['UsesThree'] == True:
            USES = True
            with open('data.json', 'r+', encoding='utf-8') as f1:
                data1 = load(f1)

                stderr.write('\n1/2')
                PROFILE = data1['PROFILE']
                PROFILEMOVE = data1['PROFILEMOVE']
                PROFILEBACK = getcwd()
                IMAGE = data1['Image']
                move(PROFILE, PROFILEBACK)

                text = (
                    "Clear-Host\n\n"
                    "$Hellowing = @\"\n"
                    f"{IMAGE} Hello!\n"
                    "\"@\n\n"
                    "Write-Host $Hellowing\n"
                )

                with open('Microsoft.PowerShell_profile.ps1', 'w', encoding='utf-8-sig') as f2:
                    f2.write(text)
                    stderr.write('\n2/2')
            move('Microsoft.PowerShell_profile.ps1', PROFILEMOVE)
        else:
            pass

    if USES == True:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = load(f)

            data['UsesThree'] = True
            with open('data.json', 'w', encoding='utf-8') as f1:
                dump(data, f1, ensure_ascii=False, indent=4)