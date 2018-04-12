import requests
from lxml import objectify

api_url = "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale"

fuelprice_data = requests.get(api_url)
root = objectify.fromstring(fuelprice_data.content)

for each_item in root.channel.item:
    print(each_item.title)
