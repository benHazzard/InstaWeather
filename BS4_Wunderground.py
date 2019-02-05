from bs4 import BeautifulSoup

from urllib.request import urlopen

hourlyWeather = []

html = urlopen("https://www.wunderground.com/hourly/us/vt/burlington")

soup = BeautifulSoup(html, 'lxml')

table_temps = soup.find('tbody').find_all('td')

indexInc=0

for x in range(7):
    c = {
        'time' : table_temps[0+indexInc].find_all('span')[0].text.strip(),
        'condition' : table_temps[1+indexInc].find_all('span')[0].text.strip(),
        'temp' : table_temps[2+indexInc].find_all('span')[0].text.strip(),
        'feelsLike' : table_temps[3+indexInc].find_all('span')[0].text.strip(),
        'precip' : table_temps[4+indexInc].find_all('span')[0].text.strip()
        }
    hourlyWeather.append(c)
    indexInc = indexInc+11
print(hourlyWeather)
print(hourlyWeather[1])


