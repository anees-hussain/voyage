from pywinauto import application
import pyautogui as pag
from time import sleep

voyageApp = "D:/Softs/CCI-Voyage-20180813T164432Z-001/CCI-Voyage/CCIVoyagePAKISTAN/CCIVoyagePAKISTAN.exe"
mediapath = "D:/_projects/python/voyage/media"

def voyage_login():
    try:
        process_id = application.process_from_module(voyageApp)

        voyageIcon = pag.locateCenterOnScreen(f"{mediapath}/voyage-icon.png", confidence=0.9)
        pag.moveTo(voyageIcon.x, voyageIcon.y, 1)
        pag.click()
    except:
        application.Application(backend="uia").start(voyageApp)

        sleep(30)
        username = pag.locateCenterOnScreen(f"{mediapath}/username-field.png", confidence=0.9)
        pag.moveTo(username.x, username.y, 1)
        pag.click()

        sleep(2)
        pag.typewrite("jabbar")

        sleep(2)
        pag.hotkey("Tab")

        sleep(2)
        pag.typewrite("Roar@357")

        sleep(3)
        VoyageLoginButton = pag.locateCenterOnScreen(f"{mediapath}/voyage-login-button.png", confidence=0.9)
        pag.moveTo(VoyageLoginButton.x, VoyageLoginButton.y, 1)
        pag.click()
        
        # voyageDefinitions = pag.locateCenterOnScreen(f"{mediapath}/definitions.png", confidence=0.9)
        # while AttributeError:
        #     sleep(5)
        sleep(30)