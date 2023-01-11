import pyautogui as pag
from time import sleep


def obj_locater(img_url):
    obj_position = pag.locateCenterOnScreen(img_url, confidence=0.9)
    try:
        pag.moveTo(obj_position.x, obj_position.y)
    except AttributeError:
        print("Object not Found. System has been delayed for 10 seconds to find the object.")
        sleep(10)
        try:
            pag.moveTo(obj_position.x, obj_position.y)
        except AttributeError:
            print("Program was exit due to slow response/object not found. Please run it again.")