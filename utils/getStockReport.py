import pyautogui as pag
from time import sleep
from datetime import datetime
from .getSecondarySales import saveReportandLogout

dt = datetime.now()
mediapath = "D:/_projects/python/voyage/media"

def getCurrentStockReport():
    # Navigation to Reports
    sleep(5)
    reports = pag.locateCenterOnScreen(f"{mediapath}/reports.png", confidence=0.9)
    pag.moveTo(reports.x, reports.y, 0.5)
    pag.click()

    # Navigation to Stock Reports
    sleep(1)
    stockReport = pag.locateCenterOnScreen(f"{mediapath}/stock-reports.png", confidence=0.9)
    pag.moveTo(stockReport.x, stockReport.y, 0.5)
    pag.click()

    # Navigation to Current Stock Report
    sleep(1)
    currentStockReport = pag.locateCenterOnScreen(f"{mediapath}/currentstockreport.png", confidence=0.9)
    pag.moveTo(currentStockReport.x, currentStockReport.y, 0.5)
    pag.click()

    # Navigation to Calender for Month Selection
    sleep(9)
    pag.moveTo(993, 525) # Mouse Position for month
    pag.click()
    if dt.month == 12:
        pag.typewrite("1")
        pag.moveTo(1047, 523) # Mouse Position for year
        sleep(1)
        pag.click()
        pag.typewrite("2023")
    else:
        pag.typewrite(f"${dt.month}")

    # Current Day Selection
    sleep(1)
    pag.moveTo(1013, 525) # Mouse Position for date
    pag.click()
    pag.typewrite("1")

    # Navigation to Preview Button
    sleep(1)
    preview = pag.locateCenterOnScreen(f"{mediapath}/preview.png", confidence=0.9)
    pag.moveTo(preview.x, preview.y, 0.5)
    pag.click()

    sleep(5)
    saveReportandLogout(reportName="stock-report")