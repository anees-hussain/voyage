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

    # Date Selection for current stock report

    sleep(3)
    stockYear = pag.locateCenterOnScreen("D:/_projects/python/voyage/media/stock-year.png", confidence=0.9)
    pag.moveTo(stockYear.x - 24, stockYear.y, 0.2) # Date Selection
    pag.click()
    pag.typewrite("1")

    sleep(4)
    pag.moveTo(stockYear.x - 38, stockYear.y, 0.2) # Month Selection
    pag.click()

    if dt.month == 12:
        pag.typewrite("1")
    else:
        pag.typewrite(f"${dt.month + 1}")

    # Selection of summer stock warehouse

    sleep(2)
    warehousebutton = pag.locateCenterOnScreen(f"{mediapath}/add-button.png", confidence=0.9)
    pag.moveTo(warehousebutton.x, warehousebutton.y)
    pag.click()

    sleep(2)
    addStock = pag.locateCenterOnScreen(f"{mediapath}/summer-stock.png", confidence=0.9)
    pag.moveTo(addStock.x, addStock.y)
    pag.click()

    sleep(1)
    closeButton = pag.locateCenterOnScreen(f"{mediapath}/stock-close-button.png", confidence=0.9)
    pag.moveTo(closeButton)
    pag.click()

    # Navigation to Preview Button
    sleep(1)
    preview = pag.locateCenterOnScreen(f"{mediapath}/preview.png", confidence=0.9)
    pag.moveTo(preview.x, preview.y, 0.5)
    pag.click()

    sleep(5)
    saveReportandLogout(reportName="stock-report")