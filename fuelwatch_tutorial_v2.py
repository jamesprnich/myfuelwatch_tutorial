from lxml import objectify
import requests

api_url = "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale"

fuelprice_data = requests.get(api_url)

root = objectify.fromstring(fuelprice_data.content)

list_of_prices = []
for each_item in root.channel.item:
    list_of_prices.append(each_item.price)

list_of_prices.sort(key=int, reverse=False)
print("List Sorted: " + str(list_of_prices))

list_of_prices.sort(key=int, reverse=True)
print("List Sorted (reversed): " + str(list_of_prices))

list_of_dicts = []

for each_item in root.channel.item:
    dict_data = {
                'Price': each_item.price.text,
                'Location': each_item.location.text,
                'Address': each_item.address.text,
                'Phone': each_item.phone.text,
                'Brand': each_item.brand.text,
                'Date': each_item.date.text
            }

    list_of_dicts.append(dict_data)

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=False)
print("Dict Sorted: " + str(list_of_dicts_sorted))

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=True)
print("Dict Sorted (reversed): " + str(list_of_dicts_sorted))
