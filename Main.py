from bs4 import BeautifulSoup

from urllib.request import urlopen, Request

from PIL import Image, ImageDraw, ImageFont

import os, sys, time

import boto3

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
class DataBase:
    def __int__(self, username, password, info):
        pass
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

	
        
        fileName = 'currentWeather-'+self.timeCurrent+'.png'
        try:
            new_out = out.resize((1080, 1920))
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
def main():
    weather = GetWeather()
    try:
        weather = list(weather.wunderground())
    except:
        weather = list(weather.weatherCom())
    timeCurrent = time.strftime('%Y%m%d-%H')
    image = CreateImage(weather, timeCurrent)
    fileName = image.newImage()
    upload = S3Upload(fileName)
    upload.uploadFile()
if __name__ == "__main__":
    main()
