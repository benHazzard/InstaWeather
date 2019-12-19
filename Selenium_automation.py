from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains

import time

import os



# -*- setting chrome options to virtual iphone -*-
chrome_options = Options()

chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

chrome_options.add_argument("window-size=250,800")

driver = webdriver.Chrome('./Assets/chromedriver', options=chrome_options)

driver.get("https://www.instagram.com")

time.sleep(2)

# -*- Clicking login button on instagram homepage -*-
driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()

time.sleep(5)

# -*- Finding username/ password boxes and inputting data respectively -*-
inputElementName = driver.find_element_by_xpath("//input[contains(@name,'username')]")
inputElementName.send_keys("")

inputElementPassword = driver.find_element_by_xpath("//input[contains(@name,'password')]")
inputElementPassword.send_keys("")


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

element = driver.find_element_by_xpath("//button[@class='JdY43']")

element.send_keys(os.getcwd()+"/jpg_44.jpg")









