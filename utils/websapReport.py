from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui as pag
from time import sleep

mediapath = "D:/_projects/python/voyage/media"

# Providing options to leave browser open after program complete
options = Options()
options.add_experimental_option("detach", True)

def getBalanceFromWebSap():
    message = ''
    def getData():
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        driver.maximize_window()
        driver.get("http://cciwebsap.cci.tr/account/newlogin")
        # driver.get("http://cciwebsap.cci.tr/")

        # Logging in using credentials
        driver.find_element("xpath", "//input[@name='UserName']").send_keys("DPKMF001")
        driver.find_element("xpath", "//input[@name='Password']").send_keys("Coke@896")
        driver.find_element("xpath", "//button[@id='btnLogin']").click()

        balance = driver.find_element("xpath", "//table[@class='table table-striped']").text
        convertedBalance = balance.split(" ")
        totalLimit = convertedBalance[2]
        availableCash = convertedBalance[8]

        return f"Total Limit: {totalLimit}\nTotal Cash Available in Company: {availableCash}"

    systemTray = pag.locateCenterOnScreen(f"{mediapath}/system-tray.png", confidence=0.9)
    pag.moveTo(systemTray.x, systemTray.y, 0.5)
    pag.click()

    sleep(2)
    connectionComplete = pag.locateCenterOnScreen(f"{mediapath}/connection-complete.png", confidence=0.9)

    if connectionComplete:
        print("connected to pulse secure")
        sleep(2)
        message = getData()

    elif type(connectionComplete) != "NoneType":
        pulseSecure = pag.locateCenterOnScreen(f"{mediapath}/pulse-secure.png", confidence=0.9)
        pag.moveTo(pulseSecure.x, pulseSecure.y, 0.5)
        pag.click(button="right")

        sleep(1)
        vpnConnection = pag.locateCenterOnScreen(f"{mediapath}/vpn-connection.png", confidence=0.9)
        pag.moveTo(vpnConnection.x, vpnConnection.y, 0.5)
        pag.click()

        sleep(1)
        vpnConnectButton = pag.locateCenterOnScreen(f"{mediapath}/vpn-connect-button.png", confidence=0.9)
        pag.moveTo(vpnConnectButton.x, vpnConnectButton.y, 0.5)
        pag.click()

        sleep(10)
        proceedButton = pag.locateCenterOnScreen(f"{mediapath}/proceed.png", confidence=0.9)
        pag.moveTo(proceedButton.x, proceedButton.y, 0.5)
        pag.click()

        sleep(15)
        print("Successfully connected to Pulse Secure!")
        print("Getting Data from websap")
        sleep(2)
        message = getData()

    return message