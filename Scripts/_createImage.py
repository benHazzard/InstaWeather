#----------IMAGE CREATION IMPORTS------------
from PIL import Image, ImageDraw, ImageFont

import os, sys, time

#=============CLASS CREATES IMAGE USING INPUTTED DATA BY USING PILLOW=========
class CreateImage:
    """
    Function: __init__
    ---------------------
    function takes in the dictionary of scraped data and converts it to a list
    """
    def __init__(self, weatherReport):
        self.weatherReport = list(weatherReport)
        self.timeCurrent = time.strftime('%Y%m%d-%H')

    """
    Function: newImage
    ------------------
    creates an image using weather data: uses pillow to open a bacground image
                                         that is stored locally. Weather image
                                         that matches the corasponding weather
                                         is then appended to the image. The font
                                         is then set using the local font asset.
                                         The weather data is then appended to the
                                         image.

    returns: .jpg image to be uploaded to instagram
    """
    def newImage(self):
        print(self.weatherReport)
        #----------IMAGE 1------------
        base = Image.open('../Assets/BackgroundImages/BackgroundImage.jpg').convert('RGBA')

        txt = Image.new('RGBA', base.size, (255,255,255,0))

        #----------IMAGE 2-----------
	#UPDATE IMAGES
        imageLocation = '../Assets/WeatherImages/Image2.png'

        if(self.weatherReport[0].get('condition', '') == 'Cloudy'):
            imageLocation = '../Assets/WeatherImages/Image2.png'
        elif(self.weatherReport[0].get('condition', '') == 'Sunny'):
            imageLocation = '../Assets/WeatherImages/Image2.png'
        elif(self.weatherReport[0].get('condition', '') == 'Rainy'):
            imageLocation = '../Assets/WeatherImages/Image2.png'
        
        conditionImage = Image.open(imageLocation).convert('RGBA')

        #----------STYLE-----------

        fnt = ImageFont.truetype("../Assets/Fonts/Comfortaa-Regular.ttf",30)

        fnt2 = ImageFont.truetype("../Assets/Fonts/Comfortaa-Regular.ttf",80)

        fillBlack = (255,255,255,255)
        #---------DRAW TEXT---------

        d = ImageDraw.Draw(txt)

        d.text((70,200), "Time:", font=fnt, fill=fillBlack)

        d.text((240,200), "Condition:", font=fnt, fill=fillBlack)

        d.text((525,200), "Temp:", font=fnt, fill=fillBlack)

        d.text((700,200), "Precip: ", font=fnt, fill=fillBlack)

        d.text((880,200), "Feels Like:", font=fnt, fill=fillBlack)

        
        d.text((70, 40), "7-hour forecast", font=fnt2, fill=fillBlack)


        #--------WEATHER VALUES------------
        yValue = 300
        
        for x in range(7):
            d.text((70,yValue), self.weatherReport[x].get('time',''), font=fnt, fill=fillBlack)
            d.text((250,yValue), self.weatherReport[x].get('condition',''), font=fnt, fill=fillBlack)
            d.text((550,yValue), self.weatherReport[x].get('temp',''), font=fnt, fill=fillBlack)
            d.text((750,yValue), self.weatherReport[x].get('precip',''), font=fnt, fill=fillBlack)
            d.text((950,yValue), self.weatherReport[x].get('feelsLike', ''), font=fnt, fill=fillBlack)
            yValue = yValue+150
        d.line((10,230, 1200,230), fill=fillBlack)

        #--------ICON------------
        
        #txt.paste(conditionImage, (700, 0), conditionImage)

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
