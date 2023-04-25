import subprocess as sp
import os

OPEN_APPS = []

try:
    lista = sp.run(['powershell.exe', 'gps | ? {$_.MainWindowTitle} | Format-Table Name'], stdout=sp.PIPE).stdout.splitlines()
    for x in range(3):
        lista.pop(0)
    for app in lista:
        lis = app.decode("utf-8")
        x = lis.strip()
        if x == "WindowsTerminal" or x == '':
            pass
        else:
            OPEN_APPS.append(x)
except Exception as ex:
    print(ex)

try:
    for app in OPEN_APPS:
        sp.check_call(['powershell.exe', "Stop-Process -NAME", app], stderr=sp.PIPE)
    close = input("Do you wish to shutdown your computer ? (y / n): ")
    if close.lower() == "y":
        os.system("shutdown /s /t 1")
    else:
        exit()
except sp.CalledProcessError as ex:
    print("already closed")
    close = input("Do you wish to shutdown your computer ? (y / n): ")
    if close.lower() == "y":
        os.system("shutdown /s /t 1")
