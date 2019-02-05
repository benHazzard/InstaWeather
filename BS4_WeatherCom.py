from bs4 import BeautifulSoup

from urllib.request import urlopen

horlyweather = []

html = urlopen("https://weather.com/weather/hourbyhour/l/05401:4:US")

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
        'precip' : table_precip[x].find_all('span')[0].text.strip()
        }
    horlyweather.append(d)

print(horlyweather)


