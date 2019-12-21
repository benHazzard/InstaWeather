#-----------AUTOMATION IMPORTS------------------
import autoit

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains

import time

import os

from sys import platform

from UserInfo import username, password


#========CLASS TAKES IN THE IMAGE NAME AND UPLOADS IT TO INSTAGRAM===========
class InstagramUpload:
    """
    Function: __init__
    -------------------
    uploads file to instagram using selenium: a driver is created based off
                                              the system the user is operating
                                              on. The driver is then set to
                                              emulate an iPhone. Selenium then
                                              naviages to the upload page. Driver
                                              then uploads image and closes.
    returns: nothing
    """
    def __init__(self, fileName):
        self.fileName = "\\" + fileName
    def postImage(self):
        print('----------ATTEMPTING TO UPLOAD FILE TO INSTAGRAM-----------')
        # -*- setting chrome options to virtual iphone -*-
        chrome_options = Options()

        chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")

        chrome_options.add_argument("window-size=250,800")

        driverName = '../Assets/Drivers/'
        if platform == 'linux' or platform == 'linux2':
            driverName = driverName + 'chromedriver_linux'
        elif platform == 'darwin':
            driverName = driverName + 'chromedriver_osx'
        elif platform == 'win32':
            driverName = driverName + 'chromedriver_windows_v79'

        driver = webdriver.Chrome(driverName, options=chrome_options)

        print('----------CHROME IPHONE DRIVER CONFIGURED AND READY-----------')
        print('Waiting for page to load...')
        
        driver.get("https://www.instagram.com")

        time.sleep(5)

        # -*- Clicking login button on instagram homepage -*-
        driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()

        print('----------LOGIN BUTTON SELECTED-----------')
        print('Waiting for page to load...')

        time.sleep(5)

        # -*- Finding username/ password boxes and inputting data respectively -*-
        inputElementName = driver.find_element_by_xpath("//input[contains(@name,'username')]")
        inputElementName.send_keys(username)

        inputElementPassword = driver.find_element_by_xpath("//input[contains(@name,'password')]")
        inputElementPassword.send_keys(password)

        print('----------USERNAME AND PASSWORD ENTERED-----------')
        
        # -*- clicking login button -*-
        driver.find_element_by_xpath("//div[contains(text(),'Log In')]").click()

        print('----------LOGIN SUCCESSFUL-----------')
        print('Waiting for page to load...')
        time.sleep(5)

        try:
            driver.find_element_by_xpath("//button[contains(@class,'GAMXX')]").click()
            print('----------EXTRA POPUP FOUND AND ADVOIDED-----------')
            print('Waiting for page to load...')
            time.sleep(5)
        except:
            print('--------EXTRA POPUP NOT FOUND--------')
            
        try:
            driver.find_element_by_xpath("//button[contains(@class,'aOOlW   HoLwm')]").click()
            print('----------EXTRA POPUP FOUND AND ADVOIDED-----------')
            print('Waiting for page to load...')
            time.sleep(5)
        except:
            print('--------EXTRA POPUP NOT FOUND--------')
        # -*- exiting popup -*-
        try:
            driver.find_element_by_css_selector("body:nth-child(2) div:nth-child(1) div.HpHcz div:nth-child(3) > a._3m3RQ._7XMpj").click()
            print('----------POPUP IGNORED-----------')
            print('Waiting for page to load...')
            time.sleep(2)
        except:
            print('--------POPUP NOT FOUND--------')
        
        # -*- exiting popup -*-
        try:
            driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]").click()

            print('----------POPUP IGNORED-----------')
            print('Waiting for page to load...')

            time.sleep(5)
        except:
            print('--------POPUP NOT FOUND--------')


        # -*- removing old post -*-
        driver.find_element_by_xpath("//div[5]//a[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body//div[contains(@class,'_2z6nI')]//div//div//div[1]//div[1]//a[1]//div[1]//div[2]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//span[contains(@class,'glyphsSpriteMore_horizontal__outline__24__grey_9 u-__7')]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[contains(text(),'Delete')]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//button[contains(text(),'Delete')]").click()
        time.sleep(5)
            

        # -*- uploading local image to story -*-
        element = driver.find_element_by_xpath("//div[@class='q02Nz _0TPg']").click()
        time.sleep(1.5)
        autoit.win_active("Open") #open can change by your os language if not open change that
        time.sleep(2)
        autoit.control_send("Open", "Edit1", os.getcwd()+ self.fileName)
        time.sleep(1.5)
        autoit.control_send("Open", "Edit1", "{ENTER}")

        print('----------FILE UPLOADED SUCCESSFULY-----------')
        print('Waiting for page to load...')
        
        time.sleep(2)

        driver.find_element_by_xpath("//span[@class='Szr5J createSpriteExpand']").click()

        driver.find_element_by_xpath("//button[@class='UP43G']").click()

        print('----------FILE SUBMITTED-----------')
        print('Waiting for page to load...')

        time.sleep(2)
        
        driver.find_element_by_xpath("//button[@class='UP43G']").click()
        print('----------FILE POSTED SUCCESSFULLY-----------')
    
        driver.close()
        print('----------DRIVER HAS EXITED-----------')
