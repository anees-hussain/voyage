import pyautogui as pag
from time import sleep

mediapath = "D:/_projects/python/voyage/media"

def getMonthlySecondarySales():
    # Navigation to Reports
    sleep(5)
    reports = pag.locateCenterOnScreen(f"{mediapath}/reports.png", confidence=0.9)
    pag.moveTo(reports.x, reports.y, 0.5)
    pag.click()

    # Navigation to Sales Reports
    sleep(1)
    salesReports = pag.locateCenterOnScreen(f"{mediapath}/sales-reports.png", confidence=0.9)
    pag.moveTo(salesReports.x, salesReports.y, 0.5)
    pag.click()

    sleep(1)
    salesByProduct = pag.locateCenterOnScreen(f"{mediapath}/salesbyproduct.png", confidence=0.9)
    pag.moveTo(salesByProduct.x, salesByProduct.y, 0.5)
    pag.click()

    # Report Query & Preview
    sleep(10)
    query = pag.locateCenterOnScreen(f"{mediapath}/query.png", confidence=0.9)
    pag.moveTo(query.x, query.y, 0.5)
    pag.click()

    sleep(10)
    preview = pag.locateCenterOnScreen(f"{mediapath}/preview.png", confidence=0.9)
    pag.moveTo(preview.x, preview.y, 0.5)
    pag.click()

    saveReportandLogout(reportName="secondary-sales")

def saveReportandLogout(reportName):
    # Saving the report in desired format at local Desktop
    sleep(4)
    save = pag.locateCenterOnScreen(f"{mediapath}/save-icon.png", confidence=0.9)
    pag.moveTo(save.x, save.y, 0.5)
    pag.click()

    sleep(4)
    fileformat = pag.locateCenterOnScreen(f"{mediapath}/excel-format.png", confidence=0.9)
    pag.moveTo(fileformat.x, fileformat.y, 0.5)
    pag.click()

    sleep(4)
    options1 = pag.locateCenterOnScreen(f"{mediapath}/data-only.png", confidence=0.9)
    pag.moveTo(options1.x, options1.y, 0.5)
    pag.click()

    sleep(1)
    options2 = pag.locateCenterOnScreen(f"{mediapath}/page-breaks.png", confidence=0.9)
    pag.moveTo(options2.x, options2.y, 0.5)
    pag.click()

    sleep(1)
    options3 = pag.locateCenterOnScreen(f"{mediapath}/continous.png", confidence=0.9)
    pag.moveTo(options3.x, options3.y, 0.5)
    pag.click()

    sleep(1)
    ok = pag.locateCenterOnScreen(f"{mediapath}/ok.png", confidence=0.9)
    pag.moveTo(ok.x, ok.y, 0.5)
    pag.click()

    sleep(5)
    desktop = pag.locateCenterOnScreen(f"{mediapath}/desktop.png", confidence=0.9)
    pag.moveTo(desktop.x, desktop.y, 0.5)
    pag.click()

    sleep(2)
    findFolder = pag.locateCenterOnScreen(f"{mediapath}/voyage-reports-folder.png", confidence=0.9)
    pag.moveTo(findFolder.x, findFolder.y, 0.5)
    pag.click()

    sleep(2)
    pag.press("enter")

    sleep(2)
    filename = pag.locateCenterOnScreen(f"{mediapath}/filename-field.png", confidence=0.9)
    pag.moveTo(filename.x, filename.y, 0.5)
    pag.click()

    pag.typewrite(reportName, 0.5)

    sleep(2)
    save = pag.locateCenterOnScreen(f"{mediapath}/save-button.png", confidence=0.9)
    pag.moveTo(save.x, save.y, 0.5)
    pag.click()

    # Closing the report and child windows
    sleep(7)
    closeReport = pag.locateCenterOnScreen(f"{mediapath}/close-report.png", confidence=0.9)
    pag.moveTo(closeReport.x, closeReport.y, 0.5)
    pag.click()

    sleep(4)
    closeWindow = pag.locateCenterOnScreen(f"{mediapath}/close-window.png", confidence=0.9)
    pag.moveTo(closeWindow.x, closeWindow.y, 0.5)
    pag.click()

    # Logging Out
    sleep(2)
    help = pag.locateCenterOnScreen(f"{mediapath}/help.png", confidence=0.9)
    pag.moveTo(help.x, help.y, 0.5)
    pag.click()

    sleep(1)
    exit = pag.locateCenterOnScreen(f"{mediapath}/exit.png", confidence=0.9)
    pag.moveTo(exit.x, exit.y, 0.5)
    pag.click()

    sleep(2)
    yes = pag.locateCenterOnScreen(f"{mediapath}/yes.png", confidence=0.9)
    pag.moveTo(yes.x, yes.y, 0.5)
    pag.click()