import autoit

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains

import time

import os

from sys import platform

# -*- setting chrome options to virtual iphone -*-
chrome_options = Options()

chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

chrome_options.add_argument("window-size=250,800")

driverName = './Assets/'
if platform == 'linux' or platform == 'linux2':
    driverName = driverName + 'chromedriver_linux'
elif platform == 'darwin':
    driverName = driverName + 'chromedriver_osx'
elif platform == 'win32':
    driverName = driverName + 'chromedriver_windows_v79'

driver = webdriver.Chrome(driverName, options=chrome_options)

driver.get("https://www.instagram.com")

time.sleep(5)

# -*- Clicking login button on instagram homepage -*-
driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()

time.sleep(5)

# -*- Finding username/ password boxes and inputting data respectively -*-
inputElementName = driver.find_element_by_xpath("//input[contains(@name,'username')]")
inputElementName.send_keys("bphazzard20@gmail.com")

inputElementPassword = driver.find_element_by_xpath("//input[contains(@name,'password')]")
inputElementPassword.send_keys("121Benman!")


# -*- clicking login button -*-
driver.find_element_by_xpath("//div[contains(text(),'Log In')]").click()

time.sleep(5)

# -*- exiting popup -*-
driver.find_element_by_css_selector("body:nth-child(2) div:nth-child(1) div.HpHcz div:nth-child(3) > a._3m3RQ._7XMpj").click()

time.sleep(2)

#driver.find_element_by_xpath("//body//div[contains(@class,'qf6s4 lGuO0')]//div//div[1]//button[1]//div[1]//span[1]//img[1]").click()

# -*- exiting popup -*-
driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]").click()

#driver.find_element_by_xpath("//nav[contains(@class,'f11OC')]//div[5]//a[1]").click()

#driver.find_element_by_xpath("//nav[contains(@class,'f11OC')]//div[5]//a[1]").click()

time.sleep(5)

# -*- uploading local image to story -*-
element = driver.find_element_by_xpath("//div[@class='q02Nz _0TPg']").click()
time.sleep(1.5)
autoit.win_active("Open") #open can change by your os language if not open change that
time.sleep(2)
autoit.control_send("Open", "Edit1", os.getcwd()+"\currentWeather-20191219-22")
time.sleep(1.5)
autoit.control_send("Open", "Edit1", "{ENTER}")
time.sleep(2)

driver.find_element_by_xpath("//button[@class='UP43G']").click()

time.sleep(2)

driver.find_element_by_xpath("//button[@class='UP43G']").click()


driver.close()






