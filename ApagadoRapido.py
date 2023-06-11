import subprocess as sp
import os
from time import sleep

class Creating_apps_list():
    def getting_apps(self):
        lista = sp.run(['powershell.exe', 'gps | ? {$_.MainWindowTitle} | Format-Table Name'], stdout=sp.PIPE).stdout.splitlines()
        return lista
    
    def listing_apps(self, lista):
        apps_not_to_close = ["WindowsTerminal", "", "SystemSettings", "TextInputHost", "ApplicationFrameHost", "Code"]
        open_apps = []
        if lista:
            for i in range(3):
                lista.pop(0)
            for app in lista:
                decode_string = app.decode("utf-8")
                program = decode_string.strip()
                if program in apps_not_to_close:
                    pass
                else:
                    open_apps.append(program)
                sleep(0.1)
        return open_apps


class Closing_apps():
    @staticmethod
    def close_apps(app_list: list[str]):
        if app_list:
            for app in app_list:
                sp.check_call(['powershell.exe', "Stop-Process -NAME", app], stderr=sp.PIPE)
                sleep(0.09)
            close = input("Do you wish to shutdown your computer ? (y / n): ")
            if close.lower() == "y":
                os.system("shutdown /s /t 1")
            else:
                exit()
        else:
            print("apps already closed")
            close = input("Do you wish to shutdown your computer ? (y / n): ")
            if close.lower() == "y":
                os.system("shutdown /s /t 1")

if __name__ == "__main__":
    apps = Creating_apps_list()
    apps_list = apps.getting_apps()
    apps_list = apps.listing_apps(apps_list)
    Closing_apps.close_apps(apps_list)
