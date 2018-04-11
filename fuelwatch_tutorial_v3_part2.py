
from lxml import objectify
import requests
import itertools
import datetime


def gen_fuelwatch_urls(fueltypes, regions, dates):

    fuelwatch_urls = [
        "http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={}&Region={}&Day={}".format(*i)
        for i in itertools.product(fueltypes, regions, dates)
    ]

    print("# of URLs to process: " + str(len(fuelwatch_urls)))
    return fuelwatch_urls


def get_fueldata(fueltypes, regions, dates):

    fuelwatch_urls = gen_fuelwatch_urls(fueltypes, regions, dates)

    list_of_dicts = []

    for each_url in fuelwatch_urls:
        print(each_url)
        fuelprice_data = requests.get(each_url)

        root = objectify.fromstring(fuelprice_data.content)

        if hasattr(root.channel, 'item'):
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
    return list_of_dicts


# ==Configuration Settings===========
# Fuelwatch API codes are located here: https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/contentholder.jspx?key=fuelwatchRSS.html
fueltypes = [11, 4, 5, ]  # 11 = Brand Diesel
regions = [2, ]  # 2 = Broome
dates = ['04/04/2018', '05/04/2018']

# Call the function to get fuel data
list_of_dicts = get_fueldata(fueltypes, regions, dates)

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=False)
print("Dict Sorted: " + str(list_of_dicts_sorted))

list_of_dicts_sorted = sorted(list_of_dicts, key=lambda k: k['Price'], reverse=True)
print("Dict Sorted (reversed): " + str(list_of_dicts_sorted))
