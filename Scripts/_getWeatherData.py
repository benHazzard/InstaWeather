#----------DATA SCRAPING AND IMAGE SCRAPING IMPORTS------------
from bs4 import BeautifulSoup

from urllib.request import urlopen, Request

#=================CLASS USES BEAUTIFULSOUP TO SCRAPE WEATHER DATA=========
class GetWeather:
    def __init(self):
        pass
    """ 
    Function: weatherCom
    ---------------------
    scrapes data from weatherCom using: beautifulsoup and stores the data in a
                                        dictonary, which is later referenced
                                        when the image is complied
                                        
    returns: dictionary of scraped weather data consisting of
             time, condition, temp, feels like, precip %
    """
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
    """ 
    Function: wunderground
    ---------------------
    scrapes data from wunderground using: beautifulsoup and stores the data in a
                                        dictonary, which is later referenced
                                        when the image is complied
                                        
    returns: dictionary of scraped weather data consisting of
             time, condition, temp, feels like, precip %
    """
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
