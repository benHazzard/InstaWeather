
#----------DATA SCRAPING AND IMAGE SCRAPING IMPORTS------------
from bs4 import BeautifulSoup

from urllib.request import urlopen, Request

from PIL import Image, ImageDraw, ImageFont

import os, sys, time

import boto3

#-----------AUTOMATION IMPORTS------------------
import autoit

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains

import time

import os

from sys import platform

from UserInfo import username, password


class GetWeather:
    def __init(self):
        pass
    def weatherCom(self):
        horlyweather = []

        hdr = {'User-Agent': 'Mozilla/5.0'}

        req = Request("https://weather.com/weather/hourbyhour/l/05401:4:US", headers=hdr)

        html = urlopen(req)

        soup = BeautifulSoup(html, 'lxml')

        table_times = soup.find_all('span', {"class":"dsx-date"})

        table_condition = soup.find_all('td', {'class':'hidden-cell-sm description'})

        table_temps = soup.find_all('td', {'class':'temp'})

        table_feels = soup.find_all('td', {'class':'feels'})

        table_precip = soup.find_all('td', {'class':'precip'})

        for x in range(7):
            d = {
                'time' : table_times[x].text.strip(),
                'condition' : table_condition[x].find_all('span')[0].text.strip(),
                'temp' : table_temps[x].find_all('span')[0].text.strip(),
                'feelsLike' : table_feels[x].find_all('span')[0].text.strip(),
                'precip' : table_precip[x].find_all('span', {'class' : ''})[0].find_all('span')[0].text.strip()
                }
            horlyweather.append(d)
        print("------------USING WEAHTERCOM------------")
        return(horlyweather)

    def wunderground(self):
        hourlyWeather = []

        html = urlopen("https://www.wunderground.com/hourly/us/vt/burlington")

        soup = BeautifulSoup(html, 'lxml')

        table_temps = soup.find('tbody').find_all('td')

        indexInc=0

        for x in range(7):
            c = {
                'time' : table_temps[0+indexInc].find_all('span')[0].text.strip(),
                'condition' : (table_temps[1+indexInc].find_all('span')[0].text.strip()).splitlines()[0],
                'temp' : table_temps[2+indexInc].find_all('span')[0].text.strip(),
                'feelsLike' : table_temps[3+indexInc].find_all('span')[0].text.strip(),
                'precip' : table_temps[4+indexInc].find_all('span')[0].text.strip()
                }
            hourlyWeather.append(c)
            indexInc = indexInc+11
        print("------------USING WUNDERGROUND------------")
        return(hourlyWeather)
class CreateImage:
    def __init__(self, weatherReport, timeCurrent):
        self.weatherReport = list(weatherReport)
        self.timeCurrent = timeCurrent
        
    def newImage(self):
        print(self.weatherReport)
        #----------IMAGE 1------------
        base = Image.open('Background-Images/Background-Image-2.2.png').convert('RGBA')

        txt = Image.new('RGBA', base.size, (255,255,255,0))

        #----------IMAGE 2-----------
	#UPDATE IMAGES
        imageLocation = 'Weather-Images/Image2.png'

        if(self.weatherReport[0].get('condition', '') == 'Cloudy'):
            imageLocation = 'Weather-Images/Cloudy.png'
        elif(self.weatherReport[0].get('condition', '') == 'Sunny'):
            imageLocation = 'Weather-Images/Cloudy.png'
        elif(self.weatherReport[0].get('condition', '') == 'Rainy'):
            imageLocation = 'Weather-Images/Cloudy.png'
        
        conditionImage = Image.open(imageLocation).convert('RGBA')

        #----------STYLE-----------

        fnt = ImageFont.truetype("Fonts/Comfortaa-Regular.ttf",30)

        fillBlack = (255,255,255,255)
        #---------DRAW TEXT---------

        d = ImageDraw.Draw(txt)

        d.text((70,400), "Time:", font=fnt, fill=fillBlack)

        d.text((240,400), "Condition:", font=fnt, fill=fillBlack)

        d.text((525,400), "Temp:", font=fnt, fill=fillBlack)

        d.text((700,400), "Precip: ", font=fnt, fill=fillBlack)

        d.text((880,400), "Feels Like:", font=fnt, fill=fillBlack)

        yValue = 600

        #--------WEATHER VALUES------------
        for x in range(7):
            d.text((70,yValue), self.weatherReport[x].get('time',''), font=fnt, fill=fillBlack)
            d.text((250,yValue), self.weatherReport[x].get('condition',''), font=fnt, fill=fillBlack)
            d.text((550,yValue), self.weatherReport[x].get('temp',''), font=fnt, fill=fillBlack)
            d.text((750,yValue), self.weatherReport[x].get('precip',''), font=fnt, fill=fillBlack)
            d.text((950,yValue), self.weatherReport[x].get('feelsLike', ''), font=fnt, fill=fillBlack)
            yValue = yValue+200
        d.line((10,450, 1200,450), fill=fillBlack)

        #--------ICON------------
        
        txt.paste(conditionImage, (700, 0), conditionImage)

        #-------CONVERT/ SAVE IMAGE---------

        out = Image.alpha_composite(base, txt)

	
        
        fileName = 'currentWeather-'+self.timeCurrent+'.jpg'
        try:
            new_out = out.resize((1080, 1350))
            new_out.save(fileName, 'png')
            new_out.show()
        except:
            print("Error Saving: ", out)
        return fileName
class S3Upload:
    def __init__(self, fileToBeUploaded):
        
        self.fileToBeUploaded = fileToBeUploaded
        
        print(self.fileToBeUploaded)
        
    def uploadFile(self):
        try:
            Key = self.fileToBeUploaded
            
            bucketName = 'instaweather'
            
            outputName = 'worked.png'
            
            s3 = boto3.client('s3')
            
            s3.upload_file(Key, bucketName, outputName)

            print('----------FILE UPLOADED-----------')
            
        except Exception as e: 
            print('File failed to upload. Error: '+ str(e))

class InstagramUpload:
    def __init__(self, fileName):
        self.fileName = "\\" + fileName
    def postImage(self):
        print('----------ATTEMPTING TO UPLOAD FILE TO INSTAGRAM-----------')
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

        # -*- exiting popup -*-
        driver.find_element_by_css_selector("body:nth-child(2) div:nth-child(1) div.HpHcz div:nth-child(3) > a._3m3RQ._7XMpj").click()
        print('----------POPUP IGNORED-----------')
        print('Waiting for page to load...')
        time.sleep(2)
        
        # -*- exiting popup -*-
        driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]").click()

        print('----------POPUP IGNORED-----------')
        print('Waiting for page to load...')

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

        driver.find_element_by_xpath("//button[@class='UP43G']").click()

        print('----------FILE SUBMITTED-----------')
        print('Waiting for page to load...')

        time.sleep(2)
        
        driver.find_element_by_xpath("//button[@class='UP43G']").click()
        print('----------FILE POSTED SUCCESSFULLY-----------')
    
        driver.close()
        print('----------DRIVER HAS EXITED-----------')
                      
def main():
    weather = GetWeather()
    try:
        weather = list(weather.wunderground())
    except:
        weather = list(weather.weatherCom())
    timeCurrent = time.strftime('%Y%m%d-%H')
    image = CreateImage(weather, timeCurrent)
    fileName = image.newImage()
    postImage = InstagramUpload(fileName)
    postImage.postImage()
    
if __name__ == "__main__":
    main()
