import subprocess as sp
import os
from tqdm import tqdm
from time import sleep
import asyncio


class View:
    def progress_bar(self):
        bar = tqdm(total=100)
        return bar

    def client_view(self):
        print("\nShutting down open apps...")

    def asking_for_shutting_pc(self, apps_closed):
        if apps_closed == False:
            print("Apps already closed")
        question = input("Do you wish to shutdown your computer ? (y / n): ")
        return question


class Creating_apps_list:
    def getting_apps(self):
        lista = sp.run(
            ["powershell.exe", "gps | ? {$_.MainWindowTitle} | Format-Table Name"],
            stdout=sp.PIPE,
        ).stdout.splitlines()
        return lista

    def listing_apps(self, lista):
        apps_not_to_close = [
            "WindowsTerminal",
            "",
            "SystemSettings",
            "TextInputHost",
            "ApplicationFrameHost",
            "Code",
            "Name",
            "----",
        ]
        open_apps = []
        if lista:
            for app in lista:
                decode_string = app.decode("utf-8")
                program = decode_string.strip()
                if program in apps_not_to_close:
                    pass
                else:
                    open_apps.append(program)
                sleep(0.05)
            open_apps.append("Whatsapp")
        return open_apps


class ShuttingDown:
    """
    Class for the logic of shutting the apps and finally the PC
    """
    def close_apps(self, app_list: list[str]):
        """
        Received a list of apps and proceed to shut them down
        param:: app_list
        return:: Bool
        """
        result = False
        if app_list:
            for app in app_list:
                sp.check_call(
                    ["powershell.exe", "Stop-Process -NAME", app], stderr=sp.PIPE
                )
                sleep(0.09)
            result = True
        return result

    def shut_pc(self, answer):
        """
        Shut down the PC if get the right input
        param:: string
        """
        if answer.lower() == "y":
            os.system("shutdown /s /t 1")
        else:
            exit()


if __name__ == "__main__":
    # Instance Classes
    listing = Creating_apps_list()
    shutting = ShuttingDown()
    view = View()

    # Executions control
    view.client_view()
    bar = view.progress_bar()
    with bar:
        apps_list = listing.getting_apps()
        apps_list = listing.listing_apps(apps_list)
        for i in range(50):
            bar.update()
            sleep(0.01)
        ready = shutting.close_apps(apps_list)
        for i in range(50):
            bar.update()
            sleep(0.01)
        bar.close()
        answer = view.asking_for_shutting_pc(ready)
        shutting.shut_pc(answer)
