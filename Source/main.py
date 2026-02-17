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

DataSend = {
    'Image': OP,
    
    'SendToday': False,
    'PROFILE': None,
    'PROFILEMOVE': None,
    'UsesImageFile': None,
}

HOST = None

print(Author)
print('TG - t.me/alcteri')

with open('TempData.json', 'r+', encoding='utf-8') as f:
    data = load(f)

    stderr.write('Открытие файла джсон для настройки\n')
    stderr.write(str(data))

    if not data['Uses'] == True:
        stderr.write('\nФайл октрыт идет его изменениме, данное сообщение больше не увидите')
        data['Uses'] = True
        data['ForYou!'] = 'Данный файл или джсон служит для проверки. Удаления файла может сломать его'

        with open('TempData.json', 'w', encoding='utf-8') as f1:
            dump(data, f1, ensure_ascii=False, indent=4)

        # sys.stderr.write('\nСкрипт сейчас закроется, вам дальше потребуется перезапустить и следовать по инструкции')
        command = 'Write-Host "Скрипт сейчас закроется, вам дальше потребуется перезапустить и следовать по инструкции" -ForegroundColor Yellow'
        run(["powershell.exe", "-Command", command])

        exit(0)
    else:
        pass


with open('TempData.json', 'r+', encoding='utf-8') as f:
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
        DataSend['PROFILE'] = a
        stderr.write('\n2/5')
        DataSend['PROFILEMOVE'] = b
        stderr.write('\n3/5')

        with open('TempData.json', 'w', encoding='utf-8') as f3:
            dump(data, f3, ensure_ascii=False, indent=4)
            stderr.write('\n4/5')

        with open('data.json', 'w', encoding='utf-8') as f1:
            dump(DataSend, f1, ensure_ascii=False, indent=4)
            stderr.write('\n5/5')
            stderr.write('\n Сейчас вам надо будет снова перезапустить скрипт, но после того перезапуска вам надо будет запускать скрипт с аргументами для настройки')
            stderr.write('''\n
                Пример - py main.py --SendToday True start
                py main.py (start, --SendToday)
                В start просто пишите start
                В --SendToday надо поставить значение False либо True         
                ''')
            exit(0)
    else:
        pass



PROFILE = None
PROFILEMOVE = None
PROFIILEBACK = None
IMAGE = None

USES = False

stdout.write('\n0/')

with open('TempData.json', 'r+', encoding='utf-8') as f:
    data = load(f)

    if not data['UsesThree'] == True:
        USES = True
        with open('data.json', 'r+', encoding='utf-8') as f1:
            data1 = load(f1)

            stderr.write('\n1/')
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
                stderr.write('\n2/')
        move('Microsoft.PowerShell_profile.ps1', PROFILEMOVE)
    else:
        pass


if USES == True:
    with open('TempData.json', 'r', encoding='utf-8') as f:
        data = load(f)

        data['UsesThree'] = True
        with open ('TempData.json', 'w', encoding='utf-8') as f1:
            dump(data, f1, ensure_ascii=False, indent=4)