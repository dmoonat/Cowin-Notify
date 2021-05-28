import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from  bs4 import BeautifulSoup
import requests
import csv
import re
import time

phone_no = 1234567890
pincode = 123456

#tested in firefox
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

##for Chrome, uncomment below code
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://selfregistration.cowin.gov.in/')
time.sleep(1)

number=driver.find_element_by_xpath('//*[@id="mat-input-0"]')
number.send_keys(phone_no)
get_otp = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div')
get_otp.click()
time.sleep(1)

send_otp=driver.find_element_by_xpath('//*[@id="mat-input-1"]')
print()
otp=input('Enter OTP')
print()
time.sleep(0.1)
send_otp.send_keys(otp)

verify=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col/ion-grid/form/ion-row/ion-col[3]')
verify.click()
time.sleep(2)

schedule=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[2]/ion-col/ion-grid/ion-row[4]/ion-col[2]/ul/li/a')

time.sleep(1)
schedule.click()
time.sleep(1)

pincode=driver.find_element_by_xpath('//*[@id="mat-input-2"]')
pincode.send_keys(pincode)

search=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[1]/ion-col[4]/ion-button')
search.click()
time.sleep(0.2)

age=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row[2]/ion-col[1]/div/div[1]')
age.click()
