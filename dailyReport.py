import os
from time import sleep
import pywhatkit as pwk
from datetime import datetime
from login import voyage_login
from utils import getPrimarySales, getSecondarySales, getStockReport, getReportsData

primarySalePath = "C:/Users/HP/OneDrive/Desktop/voyage-reports/primary-sales.xlsx"
secondarySalePath = "C:/Users/HP/OneDrive/Desktop/voyage-reports/secondary-sales.xlsx"
stockReportPath = "C:/Users/HP/OneDrive/Desktop/voyage-reports/stock-report.xlsx"
text = ''

if os.path.isfile(stockReportPath) == True:
    sleep(5)
    text = getReportsData.getData()
elif os.path.isfile(secondarySalePath) == True:
    sleep(15)
    voyage_login()
    getStockReport.getCurrentStockReport()

    sleep(5)
    text = getReportsData.getData()
elif os.path.isfile(primarySalePath) == True:
    sleep(15)
    voyage_login()
    getSecondarySales.getMonthlySecondarySales()

    sleep(15)
    voyage_login()
    getStockReport.getCurrentStockReport()

    sleep(5)
    text = getReportsData.getData()
else:
    voyage_login()
    getPrimarySales.getMonthlyPrimarySales()

    sleep(15)
    voyage_login()
    getSecondarySales.getMonthlySecondarySales()

    sleep(15)
    voyage_login()
    getStockReport.getCurrentStockReport()

    sleep(5)
    text = getReportsData.getData()

sleep(4)
dt = datetime.now()
currentHour = dt.hour
currentMinute = dt.minute

# Sending Reports Data to WhatsApp Contact
pwk.sendwhatmsg("+923003304931", text, currentHour, currentMinute + 1)

sleep(40)
pwk.sendwhatmsg("+923007327931", text, currentHour, currentMinute + 3)

os.remove(primarySalePath)
os.remove(secondarySalePath)
os.remove(stockReportPath)
os.rmdir("C:/Users/HP/OneDrive/Desktop/voyage-reports")